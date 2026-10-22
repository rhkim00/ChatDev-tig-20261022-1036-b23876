import os
import pandas as pd
from tqdm import tqdm
import json

def load_dataset(data_limit=None, resume=False):
    data = pd.read_csv("./data/SRDD/SRDD.csv")
    if resume:
        data = data.sample(frac=1, random_state=42).reset_index(drop=True)
    else:
        data = data.sample(frac=1).reset_index(drop=True)
    return data[:data_limit] if data_limit else data

def format_question(row, idx):
    return {
        "type": "SRDD",
        "req": "code",   # enables code_generated_type in reasoning_agent (extract_code_from_text -> code_path)
        "Question": "Develop a pythonic software following description:\n" + row["Description"],
        "id": idx
    }

def run(runner, evaluator, results_dir, mode, data_limit=None, resume=False,
        data_offset=0, results_suffix=""):  # data_offset/results_suffix unused
    dataset = load_dataset(data_limit, resume=resume)
    result_path = os.path.join(results_dir, "srdd.jsonl")

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
            task = format_question(row, idx)
            if task["id"] in completed_ids:
                continue
            final_ans = runner.run_reasoning(task)

            record = {
            "id": task["id"],
            "pred": final_ans
            }
            fd.write(json.dumps(record, ensure_ascii=False) + "\n")
