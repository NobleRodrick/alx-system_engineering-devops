#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    user_response = requests.get(url)
    employeeName = user_response.json().get('name')

    todo_url = url + "/todos"
    user_response = requests.get(todo_url)
    tasks = user_response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
