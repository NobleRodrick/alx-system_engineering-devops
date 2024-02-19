#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
Requirements:
    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME",
        "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed":
        TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username":
        "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    user_response = requests.get(url)
    username = user_response.json().get('username')

    todo_url = url + "/todos"
    user_response = requests.get(todo_url)
    tasks = user_response.json()

    employee_dictionary = {employee_id: []}
    for task in tasks:
        employee_dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_id), 'w') as userFile:
        json.dump(employee_dictionary, userFile)
