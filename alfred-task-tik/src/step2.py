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
task["items"].append(
    {
        "title": title
    }
)
output = json.dumps(task)
print(output)


