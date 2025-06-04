import json

with open("node.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data["title"], data["pages"])
