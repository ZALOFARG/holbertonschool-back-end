#!/usr/bin/python3
"""
Script that retrieves and displays the progress of an
employee's TODO list
"""

import csv
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

    csv_f = f'{user_id}.csv'
    with open(csv_f, 'w', newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            task_completed_status = 'True' if task.get('completed')\
                                    else 'False'
            formatted_row = [user_id,
                             username,
                             task_completed_status,
                             task.get('title')]
            csv_writer.writerow(formatted_row)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(argv[1])
    get_employee_todo_list(employee_id)
