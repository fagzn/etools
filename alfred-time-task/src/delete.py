#!/usr/bin/python3

import json
import os

data = os.getenv('TASKLIST')
tasks = json.loads(data)
if tasks is None:
    tasks = {
        "items": [
        ]
    }

title = os.getenv("title")
result = []
for task in tasks["items"]:
    if task["title"] != title:
        result.append(task)
tasks["items"] = result
output = json.dumps(tasks)
print(output)