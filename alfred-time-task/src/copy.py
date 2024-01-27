#!/usr/bin/python3

import os
from main import consume
from db_opt import Read

data = Read()

title = os.getenv("title")
result = ""
for task in data.items:
    if task.title == title:
        result = f'time spent: {task.title} - {consume(task.consume_total())}'
        break

print(result)