import json

data = {"title": "강의노트", "pages": 30}
with open("note.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
