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
			if ops == "CANCEL":
				task.stop()
			elif ops == "START":
				task.start()
			break
	tasks.print()





