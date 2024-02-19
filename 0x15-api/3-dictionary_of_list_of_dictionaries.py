#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
Requirements:
    Records all tasks from all employees
    Format must be: { "USER_ID": [ 
        {"username": "USERNAME",
        "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME",
        "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS},
        ... ], "USER_ID":
        [{"username": "USERNAME",
        "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME",
        "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS}, ... ]}
file name must be: todo_all_employees.json
"""

import json
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"

    user_response = requests.get(base_url)
    users = user_response.json()

    employee_dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        base_url = base_url + '/todos/'
        user_response = requests.get(base_url)
        tasks = user_response.json()
        employee_dictionary[user_id] = []
        for task in tasks:
            employee_dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as employee_file:
        json.dump(employee_dictionary, employee_file)
