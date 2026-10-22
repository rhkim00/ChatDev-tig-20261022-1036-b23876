#!/usr/bin/env python
"""Score SRDD eval results like the Puppeteer/ChatDev paper.

metrics per generated software (check_srdd):
  - executability: `python3 <code>` runs w/o error (10s timeout)  [runs the code]
  - completeness : no pass/todo stub
  - consistency  : cosine( embed(requirement), embed(code) )       [OpenAI embedding]
  - alignment    : consistency*completeness if executable else -1

Aggregate over ALL 200 tasks (missing/empty pred -> 0 = failure),
and also over the 181 generated (conditional quality).

id->requirement mapping: eval shuffle has no seed, so recover the per-task
requirement prefix from the eval LOG (task order == id order) and match to the
full Description in data/SRDD/SRDD.csv.
"""
import os, re, sys, json, math, argparse
import pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT); sys.path.insert(0, ROOT)
# headless-friendly: let pygame/tkinter/matplotlib programs init w/o a display
os.environ.setdefault("SDL_VIDEODRIVER","dummy")
os.environ.setdefault("SDL_AUDIODRIVER","dummy")
os.environ.setdefault("MPLBACKEND","Agg")

LOG   = "logs/runs/srdd_evolved_20260602_084311.log"
JSONL = "results/SRDD_test/srdd.jsonl"
CSVOUT= "results/SRDD_test/srdd_scored.csv"
SRDD  = "data/SRDD/SRDD.csv"

# ---------- code_path -> requirement (robust: no id-order assumption) ----------
def build_codepath2req(log, srdd_csv):
    descs = [str(d) for d in pd.read_csv(srdd_csv)["Description"]]
    def norm(s): return re.sub(r"\s+"," ", s).strip()
    pref_idx = {}
    for d in descs:
        pref_idx.setdefault(norm(d)[:40], d)
    dpat = re.compile(r"following description:\\n(.{0,90})")
    cpat = re.compile(r"(\./logs/SRDD/[^\s'\"\)]+\.py)")
    cur_req=None; cp2req={}; matched=0
    for line in open(log, errors="ignore"):
        m = dpat.search(line)
        if m:
            p = norm(m.group(1).replace("\\n"," "))[:60]
            if len(p) >= 15:
                full = pref_idx.get(p[:40])
                if full is None:
                    for d in descs:
                        if norm(d).startswith(p[:40]): full=d; break
                if full is not None: matched += 1
                cur_req = full if full is not None else p
        for cm in cpat.finditer(line):
            cp = cm.group(1)
            if cur_req and cp not in cp2req:   # first appearance -> current task req
                cp2req[cp] = cur_req
    return cp2req, matched

# ---------- main ----------
def main(map_only=False, skip_consistency=False):
    cp2req, matched = build_codepath2req(LOG, SRDD)
    print(f"[map] code_paths mapped={len(cp2req)} | desc matched to SRDD.csv={matched}")
    if map_only:
        for cp in list(cp2req)[:3]:
            print(f"  {cp}\n     -> {cp2req[cp][:70]}")
        return

    from tasks.evaluator import BenchmarkEvaluator as BE
    rows=[json.loads(l) for l in open(JSONL) if l.strip()]
    print(f"[score] {len(rows)} results | consistency={'OFF' if skip_consistency else 'ON(OpenAI)'}")

    def tofloat(x):
        try: return float(x.item()) if hasattr(x,"item") else float(x)
        except Exception: return float("nan")

    out=[]
    for r in rows:
        rid=r.get("id"); pred=(r.get("pred") or "").strip()
        rec=dict(id=rid, has_code=int(bool(pred)),
                 executability=0, completeness=0, consistency=0.0, alignment=0.0)
        if pred and os.path.exists(pred):
            try: code = open(pred, encoding="utf-8", errors="ignore").read()
            except Exception: code = ""
            try: rec["completeness"] = tofloat(BE.srdd_completeness(code))
            except Exception as e: rec["err"] = "comp:"+str(e)[:40]
            try:
                ex,_ = BE.srdd_executability(pred); rec["executability"] = 1 if ex else 0
            except Exception as e: rec["err"] = "exec:"+str(e)[:40]
            if not skip_consistency:
                req = cp2req.get(pred, "")
                if req and code:
                    try: rec["consistency"] = tofloat(BE.srdd_consistency(req, code))
                    except Exception as e: rec["err"] = "cons:"+str(e)[:40]
            rec["alignment"] = (rec["consistency"]*rec["completeness"]) if rec["executability"] else -1.0
        out.append(rec)
        if len(out)%20==0: print(f"   scored {len(out)}/{len(rows)} ...", flush=True)

    df=pd.DataFrame(out)
    df.to_csv(CSVOUT, index=False)
    N=len(df); G=int(df["has_code"].sum())
    def m(col, denom):
        return df[col].sum()/denom if col!="consistency" else df[col].sum()/denom
    print("\n"+"="*60+"\n[SRDD ACCURACY — 논문식]\n"+"="*60)
    print(f"전체 task: {N} | 코드 생성됨: {G} | 빈 결과(fail): {N-G}\n")
    print(f"{'metric':14s} {'over 200':>12s} {'over '+str(G):>12s}")
    for col in ["executability","completeness","consistency"]:
        over200=df[col].sum()/N
        overG  =df[df['has_code']==1][col].sum()/max(G,1)
        print(f"{col:14s} {over200:11.3f} {overG:11.3f}")
    al200=df["alignment"].clip(lower=0).sum()/N      # alignment: clip -1 to 0 for 'accuracy'
    alG  =df[df['has_code']==1]["alignment"].clip(lower=0).sum()/max(G,1)
    print(f"{'alignment':14s} {al200:11.3f} {alG:11.3f}   (consistency*completeness, 실행성공시)")
    print(f"\nCSV: {CSVOUT}")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--map-only", action="store_true")
    ap.add_argument("--skip-consistency", action="store_true")
    a=ap.parse_args()
    main(map_only=a.map_only, skip_consistency=a.skip_consistency)
