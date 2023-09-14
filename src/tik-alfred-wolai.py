import http.client
import json
import os

token = os.getenv('WOLAI_TOKEN')
id = os.getenv('WOLAI_DB_ID')

title = os.getenv('title')
timer = int(os.getenv('time'))

conn = http.client.HTTPSConnection("openapi.wolai.com")
payload = json.dumps({
    "rows": [
        {
            "title": title,
            "time": timer,
        }
    ]
})

headers = {
    'Authorization': f'{token}',
    'User-Agent': 'alfred',
    'Content-Type': 'application/json'
}
conn.request("POST", f"/v1/databases/{id}/rows", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))