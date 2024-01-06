import json
import sys
import time

query = sys.argv


def exist(name:str)-> bool:
    return False


def run():
    if len(query) > 1:
        item = query[1]
        if exist(item):
            # update
            print("update")
            pass
        else:
            # create
            # print("create", item)
            now = int(time.time())
            result = {
                # "rerun": 0, # 重新运行间隔
                "items":[
                    {
                        "uid": f"{item}",
                        "type": "file",
                        "title": item,
                        "subtitle": f"create a new task {item}",
                        "variables": {
                            'title': item,
                            "time": now,
                            "OPTION_TYPE": "ADD",
                        },
                    }
                ]
            }
            print(json.dumps(result))
run()


