import json
import os
import sys
import time

query = sys.argv
tasks = {}
item = ""


def init_env():
    global tasks
    global item
    proj_path = os.getenv("alfred_workflow_cache")
    data_path = f"{proj_path}/task.json"
    with open(data_path) as file:
        tasks = json.loads(file.read())

    if len(query) > 1:
        item = query[1]
def like(name:str)->[]:
    result = []
    for task in tasks["items"]:
        if task["title"].find(name) > -1:
            task["variables"] = {
                'title': task["title"],
                "OPERATION": "OPT",
            }
            result.append(task)
    return result

def run():
    tasks = like(item)
    if len(tasks) != 0:
       output_items(tasks)
    else:
        # create
        # print("create", item)
        now = int(time.time())
        output_items([
                {
                    "uid": f"{item}",
                    "type": "file",
                    "title": item,
                    "subtitle": f"create a new task {item}",
                    "variables": {
                        'title': item,
                        "time": now,
                        "OPERATION": "ADD",
                    },
                }
            ])
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

def moke():
    global tasks
    global item
    tasks = {"items": [{"uid": "asdfasdf ", "title": "asdfasdf "}]}
    item = "d"


if __name__ == '__main__':
    init_env()
    # moke()
    run()
