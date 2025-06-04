import json

s = '{"name": "홍길동", "age": 23, "passed": true}'
obj = json.loads(s)
print(obj["name"], obj["age"], obj["passed"])
