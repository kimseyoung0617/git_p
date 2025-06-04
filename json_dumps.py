import json

data = {
        "name": "김철수",
        "age": 21,
        "scores": [88, 92, 75]
}

s1 = json.dumps(data)
print(s1)

s2 = json.dumps(data, ensure_ascii=False, indent=2)
print(s2)
