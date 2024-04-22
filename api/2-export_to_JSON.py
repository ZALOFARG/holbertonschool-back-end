#!/usr/bin/python3
"""
Script that retrieves and displays the progress of an
employee's TODO list
"""

import json
import requests
from sys import argv


def get_employee_todo_list(employee_id):
    """
    Fetches and displays the employee's todo list

    Args:
        employee_id(int): the ID of the employee
    """

    base_url = 'https://jsonplaceholder.typicode.com/'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    task_list = []
    for task in todos_data:
        task_title = task.get('title')
        task_status = task.get('completed')
        task_dict = {
            "task": task_title,
            "completed": task_status,
            "username": username
        }
        task_list.append(task_dict)

    json_data = {str(user_id): task_list}

    json_f = f'{user_id}.json'
    with open(json_f, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(argv[1])
    get_employee_todo_list(employee_id)
