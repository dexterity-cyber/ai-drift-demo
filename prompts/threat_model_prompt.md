
# RULES:
# Only output pure JSON. No explanations. No extra text. No comments.
# JSON must be syntactically correct.
# Respond ONLY inside {{ ... }} object.

Your output must match this format exactly:

{{
  "summary": "short description",
  "risks": [
    {{
      "asset": "asset name",
      "threat": "threat description",
      "severity": "LOW | MEDIUM | HIGH",
      "mitigation": "mitigation description"
    }}
  ]
}}

Architecture Input:
{diagram_text}
