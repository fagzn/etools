import http.client
import json
import time
import os
import sys

query = sys.argv


token = os.getenv('WOLAI_TOKEN')
id = os.getenv('WOLAI_DB_ID')
timer = int(round(time.time() * 1000))


def create_item(item):
    return [{
        "uid": f"{item}",
        "type": "file",
        "title": f"{item}",
        "subtitle": f"create item {item}",
        "arg": "",
        "autocomplete": "",
        "icon": {
            "type": "fileicon",
            "path": "~/Desktop"
        },
        "variables": {
            'title': item,
            "time": timer,
            "OPTION_TYPE": "create",
        },
    }]


def add_item(key, count):
    return {
        "uid": key,
        "type": "file",
        "title": key,
        "subtitle": count,
        "arg": "",
        "autocomplete": "",
        "icon": {
            "type": "fileicon",
            "path": "~/Desktop"
        },
        "variables": {
            'title': key,
            "time": timer,
            "OPTION_TYPE": "add",
        },
    }


def read_wolai():
    conn = http.client.HTTPSConnection("openapi.wolai.com")
    payload = ''
    headers = {
        'Authorization': f'{token}',
        'User-Agent': 'alfred'
    }
    conn.request("GET", f"/v1/databases/{id}", payload, headers)
    res = conn.getresponse()
    data = res.read()

    response = eval(data.decode("utf-8"))
    rows = response["data"]["rows"]

    titleGroup = {}
    for i in rows:
        title = i["data"]["title"]["value"]
        if title == "":
            continue
        if title in titleGroup:
            titleGroup[title] += 1
        else:
            titleGroup[title] = 1

    items = []
    for key, count in titleGroup.items():
        item = add_item(key, count)
        items.append(item)

    return items


def show_list(items):
    result = {"items": items}
    result_json = json.dumps(result)
    print(result_json)


wolai_items = read_wolai()


def input_in_wolai(req):
    items = []
    for i in wolai_items:
        if i["title"].find(req) > -1:
            items.append(i)

    return items


if len(query) > 1:
    item = query[1]
    items = input_in_wolai(item)
    if len(items) == 0:
        items = create_item(item)
else:
    items = read_wolai()

show_list(items)