#!/usr/bin/python3

import json
import os
import time

title = os.getenv("title")
now = int(time.time())
items = [
    {
        "title": f"启动 {title}",
        "subtitle": f"启动一个新任务",
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
        "title": f"停止 {title}",
        "subtitle": f"停止当前任务",
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

