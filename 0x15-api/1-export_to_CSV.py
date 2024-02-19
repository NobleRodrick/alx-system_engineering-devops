#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME",
        "TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""

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

    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'),
                               task.get('title')))
