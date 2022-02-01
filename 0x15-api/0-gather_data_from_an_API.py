#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID.
The script must display on the standard output the employee TODO list progress
in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE
(with 1 tabulation and 1 space before the TASK_TITLE)
"""
import requests
from sys import argv


if __name__ == "__main__":
    id_emp = argv[1]

    path = "https://jsonplaceholder.typicode.com/"
    user = requests.get(path + "users/", params={"id": id_emp}).json()
    tasks = requests.get(path + "todos/", params={"userId": id_emp}).json()

    name = user[0].get("name") if len(user) > 0 else None
    tasks_d = [task.get('title') for task in tasks
               if task.get('completed') is True]
    tasks_t, tasks_c = len(tasks), len(tasks_d)

    print("Employee {} is done with tasks({}/{}):".format(name, tasks_c,
                                                          tasks_t))
    [print("\t {}".format(task)) for task in tasks_d]
