#!/usr/bin/python3

import json
import os
from db_opt import Read

taskdb = Read()

title = os.getenv("title")
create_at = os.getenv("create_at")
time = os.getenv("time")
consume = os.getenv("consume")
if consume != "":
    consume = json.loads(consume)

this = {
    "title": title,
    "create_at": int(create_at),
    "time": int(time),  # 上次截止日期
    "consumes": consume
}

taskdb.append(this)
taskdb.print()


