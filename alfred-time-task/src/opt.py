import json
import os
import sys
import time

title = os.getenv("title")
now = int(time.time())
items = [
    {
        "title": f"Start {title}",
        "subtitle": f"start a new time",
        "icon": {
              "path": './add.png',
            },
        "variables": {
            'title': title,
            "time": now,
            "SUB_OPERATION": "START",
        },
    },
    {
        "title": f"End {title}",
        "subtitle": f"end a new time",
        "icon": {
              "path": './cancel.png',
            },
        "variables": {
            'title': title,
            "time": now,
            "SUB_OPERATION": "END",
        },
    }
]


def output_items(result:any):
    if type(result) == list:
        result =  {
            "rerun": 0,  # 重新运行间隔
            "items": result,
        }
    elif type(result) == dict:
        if "items" in result:
            pass
        else:
            result = {
                "rerun": 0,  # 重新运行间隔
                "items": [result],
            }
    print(json.dumps(result))


output_items(items)

