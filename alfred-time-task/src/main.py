import json
import os
import sys
import time
from pathlib import Path

query = sys.argv
tasks = {}
item = ""

def init_env():
    global tasks
    global item
    proj_path = os.getenv("alfred_workflow_cache")
    data_path = f"{proj_path}/task.json"
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
        tasks = json.loads(file.read())

    if len(query) > 1:
        item = query[1]


def like(name:str)->[]:
    result = []
    if "items" not in tasks:
        return result
    for task in tasks["items"]:
        if task["title"].find(name) > -1:
            total = 0
            times = 0
            if "consume" in task:
                consumer = json.loads(task["consume"])
                times = len(consumer["log"])
                for i in consumer["log"]:
                    total += i["consumer"]
            startAt = int(task["time"])
            item = {
                "title": task["title"],
                "subtitle": f'已执行次数:{times},累计耗时：{consume(total)}',
                "variables": {
                    'title': task["title"],
                },
            }
            if startAt != 0:
                item["subtitle"] += f',本次开始时间:{format_date(startAt)}. 已消耗时间:{consume(int(time.time()) - startAt)}'
                item["icon"] = {
                    "path": './cancel.png',
                }
                item["variables"]["OPERATION"] = "CANCEL"
            else:
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
    tasks = like(item)
    if len(tasks) != 0:
       output_items(tasks)
    else:
        # create
        # print("create", item)
        now = int(time.time())
        consume = {"log":[]}
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
