#!/usr/bin/python3

import json
import os
import sys
import time
from pathlib import Path
from db_opt import Read, TaskDataStruct

query = sys.argv
taskdb:TaskDataStruct
item = ""


def init_env():
    global taskdb
    global item
    taskdb = Read()

    if len(query) > 1:
        item = query[1]


def like(name:str)->[]:
    result = []
    if taskdb is None:
        return result
    for index, task in enumerate(taskdb.items):
        if task.title.find(name) > -1:
            total = 0
            times = 0
            for i in task.consumes:
                total += i.consume
            startAt = task.time
            item = {
                "uid": index,
                "title": task.title,
                "subtitle": f'已执行次数:{times},累计耗时：{consume(total)}',
                "variables": {
                    'title': task.title,
                },
            }
            if startAt != 0:
                item["title"] = f'{task.title}'
                item["subtitle"] = f'【取消】{item["subtitle"]},本次开始时间:{format_date(startAt)}. 已消耗时间:{consume(int(time.time()) - startAt)}'
                item["icon"] = {
                    "path": './cancel.png',
                }
                item["variables"]["OPERATION"] = "CANCEL"
            else:
                item["title"] = f'{task.title}'
                item["subtitle"] = f'【重启】{item["subtitle"]}'
                item["icon"] = {
                    "path": './add.png',
                }
                item["variables"]["OPERATION"] = "START"
            result.append(item)
    return result


# 根据时间戳格式化本地时间字符串
def format_date(t: int) -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime(t))


# 计算已消耗时间
def consume(consume: int) -> str:
    # 将 consume 耗时转换成 小时，分钟.
    if consume < 60:
        consume = f"{consume}秒"
    elif consume < 60 * 60:
        second = consume % 60
        consume = f"{consume // 60}分钟{second}秒"
    else:
        rest = consume % (60 * 60)
        minute = rest // 60
        second = rest % 60
        consume = f"{consume // 60 // 60}小时{minute}分钟{second}秒"
    return consume

def run():
    tasks = like(item.strip())
    if len(tasks) != 0:
       output_items(tasks)
    else:
        # create
        # print("create", item)
        now = int(time.time())
        consume = []
        consume_data = json.dumps(consume)
        output_items([
                {
                    "uid": f"{item}",
                    "type": "file",
                    "title": item,
                    "subtitle": f"create a new task {item}",
                    "variables": {
                        'title': item,
                        "create_at": now,
                        "time": now,
                        "consume": consume_data,
                        "OPERATION": "ADD",
                    },
                }
            ])

def output_items(result:any):
    if type(result) == list:
        result =  {
            "rerun": 1,  # 重新运行间隔
            "items": result,
        }
    elif type(result) == dict:
        if "items" in result:
            pass
        else:
            result = {
                "rerun": 1,  # 重新运行间隔
                "items": [result],
            }
    print(json.dumps(result))

def moke():
    global tasks
    global item
    tasks = {"items": [{"uid": "asdfasdf ", "title": "asdfasdf "}]}
    item = "d"


if __name__ == '__main__':
    init_env()
    # moke()
    run()
