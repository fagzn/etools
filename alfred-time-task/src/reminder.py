#!/usr/bin/python3
from db_opt import Read


datas = Read()
title = []
for task in datas.items:
    if task.is_running():
        title.append(task.title)

if len(title) != 0:
    titles = ""
    for t in title:
        titles += t + "\n"
    print(titles)