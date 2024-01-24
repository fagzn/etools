import json
import os



PROJ_ROOT_PATH = os.getenv("alfred_workflow_cache")
DATA_FILE_NAME = "task.json"
TASK_CACHE_KEY = "TASKLIST"

# if __name__ == '__main__':
#     task = '{"items": [{"title": "groupuse", "create_at": "1705651301", "time": 0, "consume": [{"startAt": "1705651301", "endAt": 1705651761, "consumer": 460}]}]}'
#     result = json.loads(task.encode())
#     print(result)
#     new_person = TaskDataStruct(**result)
#     item = new_person.items[0]
#     print(item.Time, item.Title)
#     consum = item.Consume[0]
#     print(consum.StartAt, type(consum))