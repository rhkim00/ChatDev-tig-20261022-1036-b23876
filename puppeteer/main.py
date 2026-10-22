import argparse
import os
import json
import yaml
import glob
from tasks.runner import BenchmarkRunner
from tasks.evaluator import BenchmarkEvaluator
from tasks import mmlu_pro, gsm_hard, srdd, creative_writing

def main():
    parser = argparse.ArgumentParser(description="Run benchmark tasks")
    parser.add_argument("task", choices=["MMLU-Pro", "gsm-hard", "SRDD", "CW"])
    parser.add_argument("mode", choices=["validation", "test", "train"])
    parser.add_argument("--level", type=int, default=1)
    parser.add_argument("--index", type=int, default=-1)
    parser.add_argument("--data_limit", type=int, default=1)
    parser.add_argument("--personas", type=str, default="personas/personas.jsonl")
    parser.add_argument("--eval_policy", action="store_true")
    parser.add_argument("--train_policy", action="store_true")
    parser.add_argument("--load_policy", type=str, default="")
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--resume", action="store_true")
    # Multi-GPU data parallelism helpers. Together they let two processes
    # split a dataset slice without colliding on the same results file:
    #   GPU 0: --data_offset 0   --data_limit 100 --results_suffix gpu0
    #   GPU 1: --data_offset 100 --data_limit 100 --results_suffix gpu1
    # Each writes to its own MMLU-Pro_<mode>_<suffix>.jsonl; merge after.
    parser.add_argument("--data_offset", type=int, default=0)
    parser.add_argument("--results_suffix", type=str, default="")

    args = parser.parse_args()
    if args.eval_policy and args.train_policy:
        parser.error("--eval_policy and --train_policy are mutually exclusive")

    # load global config
    with open("config/global.yaml", "r") as f:
        global_config = yaml.safe_load(f)

    runner = BenchmarkRunner(args.personas, global_config)
    evaluator = BenchmarkEvaluator()

    results_dir = os.path.join(os.getcwd(), "results", f"{args.task}_{args.mode}")
    os.makedirs(results_dir, exist_ok=True)

    # change policy.json
    config_path = "config/policy.json"
    with open(config_path, 'r') as f:
        config = json.load(f)
    config["dataset_name"] = args.task
    config["dataset_mode"] = args.mode
    config['paths']["checkpoint_path"] = f"checkpoint/{args.task}_{args.mode}"
    if args.load_policy:
        config['paths']["model_path"] = args.load_policy

    if args.eval_policy:
        config["training"]["training"] = False
        config["training"]["loading"] = bool(args.load_policy)
    elif args.train_policy:
        config["training"]["training"] = True
        config["training"]["loading"] = bool(args.load_policy)

    if args.train_policy and args.resume and not args.load_policy:
        ckpt_dir = config['paths']["checkpoint_path"]
        latest = sorted(glob.glob(os.path.join(ckpt_dir, "*.pt")), reverse=True)
        if latest:
            config['paths']["model_path"] = latest[0]
            config["training"]["loading"] = True

    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

    task_map = {
        "MMLU-Pro": mmlu_pro.run,
        "gsm-hard": gsm_hard.run,
        "SRDD": srdd.run,
        "CW": creative_writing.run,
    }

    if args.task in task_map:
        for _ in range(args.epochs):
            task_map[args.task](
                runner, evaluator, results_dir, args.mode,
                args.data_limit, args.resume,
                args.data_offset, args.results_suffix,
            )
    else:
        print(f"Unknown task: {args.task}")

if __name__ == "__main__":
    main()
