#!/usr/bin/python3

import json
import os
import time
from db_opt import Read, TaskDataItemConsumeStruct


title = os.getenv("title")
ops = os.getenv("OPERATION")
if ops in ["CANCEL", "START"]:
	tasks = Read()
	for task in tasks.items:
		if task.title == title:
			oldStart = task.time
			now = int(time.time())
			if ops == "CANCEL":
				if oldStart == 0:
					# copy 的时候,会触发 cancel. 单纯 copy 时要跳过
					break
				task.time = 0
				new_consume = TaskDataItemConsumeStruct(oldStart, now, int(now)-int(oldStart))
				task.append(new_consume)
			elif ops == "START":
				task.time = now
			break
	tasks.print()





