#!/usr/bin/python3

import os
import time

from main import consume
from db_opt import Read

data = Read()

title = os.getenv("title")
result = ""
for task in data.items:
    if task.title == title:
        total = task.consume_total()
        if task.is_running():
            total += int(time.time()) - task.time
        result = f'{task.title} spent: {consume(total)}'
        break

print(result)