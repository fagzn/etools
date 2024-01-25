#!/usr/bin/python3

import json
import logging
import os
from pathlib import Path

from model import TASK_CACHE_KEY, PROJ_ROOT_PATH, DATA_FILE_NAME

logger = logging.getLogger()

# {
#     "items": [
#         {
#             "title": "groupuse",
#             "create_at": "1705651301",
#             "time": 0,
#             "consume": "{\"log\": [{\"startAt\": \"1705651301\", \"endAt\": 1705651761, \"consumer\": 460}]}"
#         }
#     ]
# }
class TaskDataItemConsumeStruct:
    start_at: int = 0
    end_at: int = 0
    consume: int = 0

    def __init__(self, start_at: int, end_at: int, consume: int):
        self.start_at = start_at
        self.end_at = end_at
        self.consume = consume


class TaskDataItemStruct:
    title: str = ""
    create_at: str = 0
    time: int = 0
    consumes: [TaskDataItemConsumeStruct]

    def __init__(self, title: str, create_at: str, time: int, consumes: [TaskDataItemConsumeStruct]):
        self.title = title
        self.create_at = create_at
        self.time = time
        self.consumes = [TaskDataItemConsumeStruct(**c) for c in consumes]

    def append(self, item: TaskDataItemConsumeStruct):
        self.consumes.append(item)


class TaskDataStruct:
    items: [TaskDataItemStruct]

    def __init__(self, items: [TaskDataItemStruct], **kwargs):
        self.items = [TaskDataItemStruct(**c) for c in items]
        self.other = kwargs

    def append(self, item: TaskDataItemStruct):
        self.items.append(item)

    def print(self):
        output = json.dumps(self, default=convert_to_dict, indent=2)
        print(output)



# 自定义函数，将对象转换为可序列化的字典
def convert_to_dict(obj):
    if isinstance(obj, TaskDataStruct):
        return obj.__dict__
    elif isinstance(obj, TaskDataItemStruct):
        return obj.__dict__
    elif isinstance(obj, TaskDataItemConsumeStruct):
        return obj.__dict__
    else:
        raise TypeError("Object of unsupported type")


def Read(data_path:str=None) -> [TaskDataStruct]:
    # 尝试读缓存
    data = os.getenv(TASK_CACHE_KEY)
    if data is not None and (not (data.strip() == "" or data.strip() == "{}" or len(data) == 0)):
        datas = json.loads(data)
        result = TaskDataStruct(**datas)
        return result
    # 读文件
    if data_path == None:
        data_path = f"{PROJ_ROOT_PATH}/{DATA_FILE_NAME}"
        directory = Path(data_path).parent

        # 检查目录是否存在，如果不存在则递归创建目录
        if not directory.exists():
            directory.mkdir(parents=True)

    if not os.path.exists(data_path):
        with open(data_path, "w") as file:
            DefaultData()

    with open(data_path) as file:
        content = file.read()
        if content.strip() == "":
            items = DefaultData()
            return items
        else:
            datas = json.loads(content)

    result = TaskDataStruct(**datas)

    return result


def Write(data:TaskDataStruct):
    output = json.dumps(data, default=convert_to_dict, indent=2)
    print(output)

def DefaultData() -> [TaskDataStruct]:
    default = TaskDataStruct([])
    # Write(default)
    return default