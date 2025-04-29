
.PHONY: setup baseline drift guardrails demo clean

PYTHON := .venv/bin/python
PIP := .venv/bin/pip

# Setup virtual environment and install dependencies
setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install langchain llama-cpp-python guardrails-ai nltk

# Generate baseline threat model
baseline:
	$(PYTHON) scripts/generate_threat_model.py --diagram diagrams/baseline.drawio --prompt prompts/threat_model_prompt.md --output baseline.json

# Generate drifted threat model
drift:
	$(PYTHON) scripts/generate_threat_model.py --diagram diagrams/tampered.drawio --prompt prompts/threat_model_prompt.md --output drift.json

# Validate drifted threat model with guardrails
guardrails:
	$(PYTHON) scripts/validate_output.py drift.json

# Full sequence demo
demo: baseline drift guardrails

# Clean environment
clean:
	rm -rf .venv baseline.json drift.json
