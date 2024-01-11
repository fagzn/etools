import json
import os
import time


title = os.getenv("title")
ops = os.getenv("OPERATION")
if ops in ["CANCEL", "START"]:
	data = os.getenv('TASKLIST')
	tasks = json.loads(data)
	if "items" in tasks:
		for task in tasks["items"]:
			if task["title"] == title:
				oldStart = task["time"]
				now = int(time.time())
				if ops == "CANCEL":
					task["time"] = 0
					consume = json.loads(task["consume"])
					consume["log"].append({"startAt": oldStart, "endAt": now, "consumer": int(now)-int(oldStart)})
					consumeData = json.dumps(consume)
					task["consume"] = consumeData
				elif ops == "START":
					task["time"] = now
				break
	taskData = json.dumps(tasks)
	print(taskData)





