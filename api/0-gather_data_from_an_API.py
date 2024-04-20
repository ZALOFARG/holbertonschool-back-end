#!/usr/bin/python3
"""
Script that retrieves and displays the progress of an
employee's TODO list
"""

import requests
from sys import argv


def get_employee_todo_list(employee_id):
    """Fetches and displays the employee's todo list

    Args:
        employee_id(int): the ID of the employee
    """

    base_url = 'https://jsonplaceholder.typicode.com/'
    url = 'https://jsonplaceholder.typicode.com/todos?userId='

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    user_name = user_data.get('name')

    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    print('Employee {} is done with ({}/{}):'.format(
        user_name, num_done_tasks, total_tasks)
        )
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == '__main__':
    employee_id = int(argv[1])
    get_employee_todo_list(employee_id)
