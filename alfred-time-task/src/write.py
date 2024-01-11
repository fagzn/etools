import json
import os
import sys
import time

data = os.getenv('TASKLIST')
task = json.loads(data)
if task is None:
    task = {
        "items": [
        ]
    }

title = os.getenv("title")
create_at = os.getenv("create_at")
time = os.getenv("time")
consume = os.getenv("consume")

this = {
    "title": title,
    "create_at": create_at,
    "time": time,  # 上次截止日期
    "consume": consume
}

task["items"].append(this)

output = json.dumps(task)
print(output)


