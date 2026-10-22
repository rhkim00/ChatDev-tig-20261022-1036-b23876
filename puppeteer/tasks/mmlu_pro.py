import os
import string
import json
import pandas as pd
from tqdm import tqdm
from tasks.base.base_task import BaseTask

def _is_training():
    try:
        with open("config/policy.json", "r") as f:
            cfg = json.load(f)
        return bool(cfg.get("training", {}).get("training", False))
    except Exception:
        return False

def load_dataset(mode, data_limit=None, data_offset=0):
    path = os.path.join("data", "MMLU-Pro", f"{mode}.parquet")
    data = pd.read_parquet(path)
    if data_offset:
        # Drop the first `data_offset` rows so two processes can take
        # disjoint slices of the same parquet without overlap.
        data = data.iloc[data_offset:].reset_index(drop=True)
    return data[:data_limit] if data_limit else data

def format_question(task):
    options = [f"{letter}: {op}" for letter, op in zip(string.ascii_uppercase, task["options"])]
    prompt = f"The following are multiple choice questions (with answers) about {task['category']}."
    question = prompt + "\n" + task["question"] + "\n" + " ".join(options)
    return {
        "type": "MMLU-Pro",
        "Question": question,
        "Answer": task["answer"],
        "id": task["question_id"]
    }

def run(runner, evaluator, results_dir, mode, data_limit=None, resume=False,
        data_offset=0, results_suffix=""):
    dataset = load_dataset(mode, data_limit, data_offset)
    # results_suffix lets two parallel workers write to separate files
    # (MMLU-Pro_test_gpu0.jsonl vs MMLU-Pro_test_gpu1.jsonl) so they don't
    # race on a shared append target. Default empty preserves old behavior.
    suffix = f"_{results_suffix}" if results_suffix else ""
    result_path = os.path.join(results_dir, f"MMLU-Pro_{mode}{suffix}.jsonl")
    acc = 0
    training = _is_training()
    save_every = 10

    completed_ids = set()
    if resume and os.path.exists(result_path):
        with open(result_path, "r", encoding="utf-8") as rf:
            for line in rf:
                try:
                    record = json.loads(line)
                    completed_ids.add(record.get("id"))
                except json.JSONDecodeError:
                    continue

    write_mode = "a" if resume and completed_ids else "w"

    with open(result_path, write_mode, encoding="utf-8") as fd:
        for idx, row in tqdm(dataset.iterrows(), total=len(dataset)):
            task = format_question(row)
            if task["id"] in completed_ids:
                continue
            final_ans = runner.run_reasoning(task)
            flag = evaluator.check_mmlu(final_ans, task["Answer"])
            if flag: 
                acc += 1
            record = {
            "id": task["id"],
            "pred": final_ans,
            "correct": flag
            }
            fd.write(json.dumps(record, ensure_ascii=False) + "\n")
            fd.flush()
            if training:
                completed_ids.add(task["id"])
                processed = len(completed_ids)
                if processed % save_every == 0 or processed == len(dataset):
                    runner.save_policy(tag=f"step_{processed}")
