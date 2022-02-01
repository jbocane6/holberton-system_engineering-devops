#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
Requirements:
Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""

import json
import requests


if __name__ == "__main__":
    path = "https://jsonplaceholder.typicode.com/"
    users = requests.get(path + "users/").json()
    tasks = requests.get(path + "todos/").json()

    all_todos = {}
    for user in users:
        id_user = user.get("id")
        task_list = [{"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": user.get("username")}
                     for task in tasks if id_user == task.get("userId")]
        all_todos[id_user] = task_list

    with open("todo_all_employees.json", "w", newline="") as f:
        json.dump(all_todos, f)
