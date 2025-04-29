# 🧠 AI Threat Modeling Gone Rogue – Live Demo

This project demonstrates how semantic drift in architecture diagrams can break AI threat modeling—and how to catch it using only open-source tools.

---

## ⚙️ 1. Clean Setup Instructions

```bash
# OPTIONAL: Clean any old venv
rm -rf .venv

# Create new virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate   # or `. .venv/bin/activate`

# Install all required packages
pip install -r requirements.txt
```

---

## 📁 2. Place Your Llama Model

Ensure the `.gguf` model file is placed inside the `models/` directory.

You can use:
- `Meta-Llama-3-8B-Instruct-Q4_K_M.gguf` (recommended)
- `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` (faster fallback)

Check your model file path:

```bash
ls models/
```

Update this path in `scripts/generate_threat_model.py`:

```python
llm = LlamaCpp(
    model_path="models/your-model-name.gguf",
```

---

## 🚀 3. Run the Demo

```bash
make baseline       # Generate threat model from baseline diagram
make drift          # Generate threat model from tampered diagram
make guardrails     # Validate drifted output using Guardrails
make demo           # Run the full pipeline
```

---

## 🛠️ Common Fixes

- **Missing LLM model file**: Double-check `model_path` matches your `.gguf` filename.
- **LangChain 0.2+**: Requires `langchain_community` to be installed (included in `requirements.txt`).
- **Makefile error: missing separator**: Ensure lines are indented with **TAB**, not spaces.

---

## 📁 Folder Structure

```
ai-drift-demo/
├── diagrams/
├── models/
├── prompts/
├── schema/
├── scripts/
├── baseline.json
├── drift.json
├── Makefile
├── requirements.txt
└── README.md
```

---

2025 – Live Demo by Deepam Kanjani
