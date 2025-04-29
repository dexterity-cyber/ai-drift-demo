"""Adversarial fuzzing of prompt using LangChain Bench + cosine drift detection."""
import argparse, json, random, sys, pathlib, re
from sentence_transformers import SentenceTransformer, util
from langchain_bench.harness import FuzzHarness

def random_swap(text):
    words = text.split()
    if len(words) < 2:
        return text
    i, j = random.sample(range(len(words)), 2)
    words[i], words[j] = words[j], words[i]
    return ' '.join(words)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prompt', required=True)
    ap.add_argument('-n', type=int, default=20)
    args = ap.parse_args()

    base_prompt = pathlib.Path(args.prompt).read_text()
    model = SentenceTransformer('all-MiniLM-L6-v2')
    base_vec = model.encode(base_prompt)

    for _ in range(args.n):
        mutated = random_swap(base_prompt)
        vec = model.encode(mutated)
        drift = float(util.cos_sim(base_vec, vec))
        if drift < 0.8:  # cosine similarity lower -> drift higher
            print('Drift detected, failing.')
            sys.exit(1)
    print('No concerning drift in fuzz run.')

if __name__ == '__main__':
    main()
