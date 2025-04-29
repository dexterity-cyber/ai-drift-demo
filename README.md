# AI Threat Modeling Gone Rogue – Demo

Reproduce the Semantic Drift exploit and guard-rail defenses with **free, open‑source tools**.

## Prerequisites
* Python 3.11+
* Make / Bash
* ≥16 GB RAM
* `cmake`, `jq` (for diff visual), `graphviz` (optional)
* Llama 3 8B *gguf* weights (download separately, ≈4 GB) → place in `models/`

## Quick Start

```bash
git clone <this‑repo>
cd ai-drift-demo
make setup          # creates venv & installs packages
make baseline       # generate baseline threat model
make drift          # generate tampered model & show diff
make guardrails     # run validation + fuzz (should fail on drift)
```

## Targets

| Make target | Action |
|-------------|--------|
| `setup`     | install Python deps + build llama.cpp |
| `baseline`  | run `generate_threat_model.py` on baseline diagram |
| `drift`     | run on tampered diagram and diff outputs |
| `guardrails`| run validation + fuzz tests |

