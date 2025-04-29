
"""Generate threat model JSON from diagram using local Llama.cpp model.""" 
import argparse
import json
import xml.etree.ElementTree as ET
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate

def extract(diagram_path: str) -> str:
    """Extract node labels (assets) from a .drawio XML file."""
    tree = ET.parse(diagram_path)
    root = tree.getroot()

    assets = []
    for cell in root.iter('mxCell'):
        value = cell.attrib.get('value')
        vertex = cell.attrib.get('vertex')
        if value and vertex == "1":
            assets.append(value.strip())

    if not assets:
        return "No assets found."

    return "The system consists of: " + ", ".join(assets) + "."

def parse_structured(text: str):
    """Extract and safely parse first JSON object from LLM output."""
    import re
    m = re.search(r'({.*})', text, flags=re.S)
    if not m:
        raise ValueError("No JSON detected")

    raw_json = m.group(1)
    raw_json = raw_json.replace('\n', '').replace('\t', '').replace(',}', '}').replace(',]', ']')

    try:
        return json.loads(raw_json)
    except Exception as e:
        print(f"[Fatal] JSON parsing failed: {e}")
        raise ValueError("Could not auto-repair JSON output.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--diagram', required=True)
    ap.add_argument('--prompt', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    llm = LlamaCpp(
        model_path="models/llama-3-8b-instruct.Q4_K_M.gguf",
        temperature=0.2,
        n_ctx=4096,
    )

    template = open(args.prompt).read()
    prompt = PromptTemplate.from_template(template).format(diagram_text=extract(args.diagram))

    for attempt in range(2):
        response = llm(prompt)
        try:
            data = parse_structured(response)
            break
        except Exception:
            print(f"[Retry] Attempt {attempt+1} failed.")
            continue
    else:
        raise ValueError("Failed to parse structured output after retries.")

    with open(args.output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f'[+] Threat model generated: {args.output}')

if __name__ == '__main__':
    main()
