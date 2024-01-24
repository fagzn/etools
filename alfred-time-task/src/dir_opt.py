#!/usr/bin/python3

import json
import os
import time
from db_opt import ReadCache, TaskDataItemConsumeStruct


title = os.getenv("title")
ops = os.getenv("OPERATION")
if ops in ["CANCEL", "START"]:
	tasks = ReadCache()
	for task in tasks.items:
		if task.title == title:
			oldStart = task.time
			now = int(time.time())
			if ops == "CANCEL":
				task.time = 0
				new_consume = TaskDataItemConsumeStruct(oldStart, now, int(now)-int(oldStart))
				task.append(new_consume)
			elif ops == "START":
				task.time = now
			break
	tasks.print()





