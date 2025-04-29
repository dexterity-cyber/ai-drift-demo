import guardrails as gd

SCHEMA_RAIL = "schema/guardrails.rail"

with open("drift.json") as f:
    raw_data = f.read()

guard = gd.Guard.from_rail(SCHEMA_RAIL)
validated_output, *rest = guard.parse(raw_data)

print("[+] Guardrails validation successful.")
print(validated_output)
