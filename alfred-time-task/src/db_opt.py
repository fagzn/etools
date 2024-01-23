#!/usr/bin/python3

import json
import os
from pathlib import Path

from model import TASK_CACHE_KEY, PROJ_ROOT_PATH, DATA_FILE_NAME,TaskDataStruct,TaskDataItemStruct


def Read(data_path:str=None) -> [TaskDataItemStruct]:
    if data_path == None:
        data_path = f"{PROJ_ROOT_PATH}/{DATA_FILE_NAME}"
        directory = Path(data_path).parent

        # 检查目录是否存在，如果不存在则递归创建目录
        if not directory.exists():
            directory.mkdir(parents=True)

    if not os.path.exists(data_path):
        with open(data_path, "w") as file:
            ctx = {"items":[]}
            ctxData = json.dumps(ctx)
            file.write(ctxData)

    with open(data_path) as file:
        datas = json.loads(file.read())

    result = TaskDataStruct(**datas)

    return result

def Write(data:TaskDataStruct):
    output = json.dump(TaskDataStruct, data)
    print(output)


def GetFlowCache():
    data = os.getenv(TASK_CACHE_KEY)
    task = json.loads(data)
    if task is None:
        task = {
            "items": [
            ]
        }
    return task
