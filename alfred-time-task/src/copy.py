#!/usr/bin/python3

import json
import os
from main import consume

data = os.getenv('TASKLIST')
tasks = json.loads(data)
if tasks is None:
    tasks = {
        "items": [
        ]
    }

title = os.getenv("title")
result = ""
for task in tasks["items"]:
    if task["title"] != title:
        total = 0
        if "consume" in task:
            consumer = json.loads(task["consume"])
            for i in consumer["log"]:
                total += i["consumer"]
        result = f'time spent: {task["title"]} - {consume(total)}'

print(result)