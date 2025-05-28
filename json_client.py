import requests

BASE = 'http://220.149.232.226:10011/api'

resp = requests.get(f'{BASE}/hello')
print(resp.status_code)
print(resp.json())

payload = {'name': 'Kevin', 'age': 90}
resp2 = requests.post(f'{BASE}/echo', json=payload)
print(resp2.status_code)
print(resp2.json())
