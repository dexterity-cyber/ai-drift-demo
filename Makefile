    VENV=.venv
    PY=$(VENV)/bin/python

    setup:
    	python -m venv $(VENV)
    	$(PY) -m pip install -U pip
    	$(PY) -m pip install -U langchain guardrails-ai rebuff textattack langchain-bench sentence-transformers
    	git clone --depth 1 https://github.com/ggerganov/llama.cpp.git || true
    	$(MAKE) -C llama.cpp

    baseline:
    	$(PY) scripts/generate_threat_model.py --diagram diagrams/baseline.drawio --prompt prompts/threat_model_prompt.md --output baseline.json

    drift:
    	$(PY) scripts/generate_threat_model.py --diagram diagrams/tampered.drawio --prompt prompts/threat_model_prompt.md --output drift.json
    	diff -u baseline.json drift.json || true

    guardrails:
    	$(PY) scripts/validate_output.py drift.json; \
	$(PY) scripts/fuzz_test.py --prompt prompts/threat_model_prompt.md --n 10
