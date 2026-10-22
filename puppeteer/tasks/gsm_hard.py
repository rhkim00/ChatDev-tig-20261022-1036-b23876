import os
import json
import pandas as pd
from tqdm import tqdm
from tasks.base.base_task import BaseTask

def load_dataset(mode, data_limit=None, resume=False):
    path = os.path.join("data", "GSM-Hard", "test.parquet")
    data = pd.read_parquet(path)
    if resume:
        data = data.sample(frac=1, random_state=42).reset_index(drop=True)
    else:
        data = data.sample(frac=1).reset_index(drop=True)
    return data[:data_limit] if data_limit else data

def format_question(row, idx):
    return {
        "type": "GSM-Hard",
        "Question": "You need to write python program to solve math problems:\n" + row["input"],
        "Answer": row["target"],
        "id": idx
    }

def run(runner, evaluator, results_dir, mode, data_limit=None, resume=False,
        data_offset=0, results_suffix=""):  # data_offset/results_suffix unused
    dataset = load_dataset(mode, data_limit, resume=resume)
    result_path = os.path.join(results_dir, "gsm-hard.jsonl")
    acc = 0

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
        for idx, row in enumerate(tqdm(dataset.iterrows(), total=len(dataset))):
            task = format_question(row[1], idx)
            if task["id"] in completed_ids:
                continue
            final_ans = runner.run_reasoning(task)
            flag = evaluator.check_gsm8k(final_ans, task["Answer"])
            if flag: acc += 1
            record = {
            "id": task["id"],
            "pred": final_ans,
            "correct": flag
            }
            fd.write(json.dumps(record, ensure_ascii=False) + "\n")
