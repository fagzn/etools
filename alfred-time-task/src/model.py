import json
import os


# {
#     "items": [
#         {
#             "title": "groupuse",
#             "create_at": "1705651301",
#             "time": 0,
#             "consume": "{\"log\": [{\"startAt\": \"1705651301\", \"endAt\": 1705651761, \"consumer\": 460}]}"
#         }
#     ]
# }
class TaskDataItemConsumeStruct:
    StartAt: str = ""
    EndAt: int = 0
    Consumer: int = 0

    def __init__(self, startAt: str, endAt: int, consumer: int):
        self.StartAt = startAt
        self.EndAt = endAt
        self.Consumer = consumer


class TaskDataItemStruct:
    Title: str = ""
    CreateAt: str = 0
    Time: int = 0
    Consumer: [TaskDataItemConsumeStruct]

    def __init__(self, title: str, create_at: str, time: int, consume: [TaskDataItemConsumeStruct]):
        self.Title = title
        self.CreateAt = create_at
        self.Time = time
        self.Consume = [TaskDataItemConsumeStruct(**c) for c in consume]


class TaskDataStruct:
    Items: [TaskDataItemStruct]

    def __init__(self, items: [TaskDataItemStruct], **kwargs):
        self.items = [TaskDataItemStruct(**c) for c in items]
        self.Other = kwargs


PROJ_ROOT_PATH = os.getenv("alfred_workflow_cache")
DATA_FILE_NAME = "task.json"
TASK_CACHE_KEY = "TASKLIST"

if __name__ == '__main__':
    task = '{"items": [{"title": "groupuse", "create_at": "1705651301", "time": 0, "consume": [{"startAt": "1705651301", "endAt": 1705651761, "consumer": 460}]}]}'
    result = json.loads(task.encode())
    print(result)
    new_person = TaskDataStruct(**result)
    item = new_person.items[0]
    print(item.Time, item.Title)
    consum = item.Consume[0]
    print(consum.StartAt, type(consum))