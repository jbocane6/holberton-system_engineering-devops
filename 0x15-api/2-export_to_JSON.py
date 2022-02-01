#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
Requirements:
Records all tasks that are owned by this employee
Format must be:{ "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    id_emp = argv[1]

    path = "https://jsonplaceholder.typicode.com/"
    user = requests.get(path + "users/", params={"id": id_emp}).json()
    tasks = requests.get(path + "todos/", params={"userId": id_emp}).json()

    username = user[0].get("username") if len(user) > 0 else None
    task_list = [{"task": task.get('title'),
                  "completed": task.get('completed'),
                  "username": username} for task in tasks]

    with open("{}.json".format(id_emp), "w", newline="") as f:
        json.dump({id_emp: task_list}, f)
