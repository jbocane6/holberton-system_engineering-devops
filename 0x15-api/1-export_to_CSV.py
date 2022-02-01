#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the CSV format.
Requirements:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    id_emp = argv[1]

    path = "https://jsonplaceholder.typicode.com/"
    user = requests.get(path + "users/", params={"id": id_emp}).json()
    tasks = requests.get(path + "todos/", params={"userId": id_emp}).json()

    username = user[0].get("username") if len(user) > 0 else None
    record = [[id_emp, username, task.get('completed'), task.get('title')]
              for task in tasks]

    with open("{}.csv".format(id_emp), "w", newline="") as f:
        file_out = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        file_out.writerows(record)
