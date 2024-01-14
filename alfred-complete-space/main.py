#!/usr/bin/python3 main.py

import json
import os
import re
import sys
import time
from pathlib import Path

# 第一参数是文件,第二个参数是文件路径,第三个参数才是用户输入参数
query = sys.argv


def is_valid_path(url):
    # 一个简单的正则表达式来匹配URL
    pattern = r'[~\w\/]+[\w.\s]+'

    # 使用正则表达式匹配URL
    match = re.match(pattern, url)

    return bool(match)

def replace_space(path):
    return path.replace(" ", "\\ ")

def output_items(result:any):
    if type(result) == list:
        result =  {
            "rerun": 0,  # 重新运行间隔
            "items": result,
        }
    elif type(result) == dict:
        if "items" in result:
            pass
        else:
            result = {
                "rerun": 0,  # 重新运行间隔
                "items": [result],
            }
    print(json.dumps(result))

if len(query) > 2:
    path = query[2]
    if path != "" and is_valid_path(path):
        newPath = replace_space(path)
        output_items([
            {
                "uid": "122",
                "type": "file",
                "title": newPath,
                "variables": {
                    'title': newPath,
                },
            }
        ])


if __name__ == '__main__':
    pass