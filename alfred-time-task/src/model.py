import os


# alfred 的缓存目录
PROJ_ROOT_PATH = os.getenv("alfred_workflow_cache")
# 数据文件名称
DATA_FILE_NAME = "task.json"
# 数据链路上缓存的key
TASK_CACHE_KEY = "TASKLIST"
# reminder 的 key
REMINDER_KEY = "REMINDER"
REMINDER_VALUE_GIVEUP = "giveup"
REMINDER_VALUE_CONTINUE = "continue"
