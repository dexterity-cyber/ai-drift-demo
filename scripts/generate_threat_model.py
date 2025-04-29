"""Generate threat model JSON from diagram using local Llama.cpp model."""
import argparse, json, pathlib, re
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate

def extract(diagram_path: str) -> str:
    """Naïve extractor that returns raw XML for demo purposes."""
    return pathlib.Path(diagram_path).read_text()[:4000]

def parse_structured(text: str):
    """Extract first JSON object found in LLM output."""
    m = re.search(r'{.*}', text, flags=re.S)
    if not m:
        raise ValueError("No JSON detected")
    return json.loads(m.group(0))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--diagram', required=True)
    ap.add_argument('--prompt', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    llm = LlamaCpp(
        model_path=str(pathlib.Path('models/llama-3-8b-instruct.Q4_K_M.gguf')),
        temperature=0.2,
        n_ctx=4096,
        verbose=False
    )

    template = pathlib.Path(args.prompt).read_text()
    prompt = PromptTemplate.from_template(template).format(diagram_text=extract(args.diagram))
    response = llm(prompt)
    data = parse_structured(response)

    pathlib.Path(args.output).write_text(json.dumps(data, indent=2))
    print(f'Wrote {args.output}')

if __name__ == '__main__':
    main()
