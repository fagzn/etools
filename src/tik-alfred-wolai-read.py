import http.client
import json
import time
import os

token = os.getenv('WOLAI_TOKEN')
id = os.getenv('WOLAI_DB_ID')

time = int(round(time.time() * 1000))

conn = http.client.HTTPSConnection("openapi.wolai.com")
payload = ''
headers = {
    'Authorization': f'{token}',
    'User-Agent': 'alfred'
}
conn.request("GET", f"/v1/databases/{id}", payload, headers)
res = conn.getresponse()
data = res.read()

response = eval(data.decode("utf-8"))
rows = response["data"]["rows"]

titleGroup = {}
for i in rows:
    title = i["data"]["title"]["value"]
    if title == "":
        continue
    if title in titleGroup:
        titleGroup[title] += 1
    else:
        titleGroup[title] = 1

items = []
for key, count in titleGroup.items():
    items.append({
        "uid": key,
        "type": "file",
        "title": key,
        "subtitle": count,
        "arg": "",
        "autocomplete": "",
        "icon": {
            "type": "fileicon",
            "path": "~/Desktop"
        },
        "variables": {
            'title': key,
            "time": time
        },
    })

result = {"items": items}

result_json = json.dumps(result)
print(result_json)

