# 🧠 AI Threat Modeling Gone Rogue – Live Demo

This project demonstrates how semantic drift in architecture diagrams can break AI threat modeling—and how to catch them using only open-source tools.

---

## ⚙️ 1. First-Time Setup (Fresh Clone)

Use the provided bootstrap script:

```bash
bash bootstrap.sh
```

This will:
- Create `.venv`
- Install all packages from `requirements.txt`
- Check for presence of a `.gguf` model

---

## ♻️ 2. Reset Your Environment Anytime

To reset the environment and start fresh:

```bash
bash reset.sh
```

This will:
- Delete `.venv`, `baseline.json`, and `drift.json`
- Recreate the environment
- Reinstall all dependencies

---

## 📁 3. Place Your Llama Model

Ensure the `.gguf` model file is placed inside the `models/` directory.

You can use:
- `llama-3-8b-instruct.Q4_K_M.gguf` (recommended)
- `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` (faster fallback)

Then edit `scripts/generate_threat_model.py`:

```python
llm = LlamaCpp(
    model_path="models/your-model-name.gguf",
```

---

## 🚀 4. Run the Demo

```bash
make baseline       # Generate threat model from baseline diagram
make drift          # Generate threat model from tampered diagram
make guardrails     # Validate drifted output using Guardrails
make demo           # Run the full pipeline
```

---

## 🛠️ Common Fixes

- **Missing model file**: Confirm your `model_path` matches the `.gguf` file in `models/`.
- **LangChain 0.2+**: Requires `langchain_community` installed (included in `requirements.txt`).
- **Makefile errors**: Ensure lines are indented using **TAB**, not spaces.

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
├── reset.sh
├── bootstrap.sh
└── README.md
```

---

2025 – Live Demo by Deepam Kanjani