"""Validate JSON output against glossary using Guardrails-AI."""
import guardrails as gd, json, argparse, pathlib, sys

GLOSSARY = ["PublicAPI", "Database", "AuthService", "InternalService"]

SCHEMA_YAML = f"""
type: object
properties:
  risks:
    type: array
    items:
      properties:
        asset:
          enum: {GLOSSARY}
        threat: {{type: string}}
        severity: {{enum: ["LOW", "MEDIUM", "HIGH"]}}
        mitigation: {{type: string}}
"""

guard = gd.Guard.from_yaml(SCHEMA_YAML)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file')
    args = ap.parse_args()
    data = json.loads(pathlib.Path(args.file).read_text())
    guard.validate(data)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Guardrails validation failed: {e}')
        sys.exit(1)
