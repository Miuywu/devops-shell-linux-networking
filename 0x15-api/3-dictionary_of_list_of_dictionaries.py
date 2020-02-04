#!/usr/bin/python3
""" uses REST API to take in employee ID returns TODO list info """

import json
import requests
from sys import argv

if __name__ == "__main__":
    rURL = "https://jsonplaceholder.typicode.com/users/"
    all_users = requests.get(rURL).json()
    rURL2 = "https://jsonplaceholder.typicode.com/todos"
    all_todos = requests.get(rURL2).json()

    big_dict = {}
    for user in all_users:        
        todo_list = []
        user_id = user.get('id')
        for todo in all_todos:
            if todo.get('userId') == user_id:
                list_entry = {}
                list_entry["username"] = user.get('username')
                list_entry["task"] = todo.get('title')
                list_entry["completed"] = todo.get('completed')
                todo_list.append(list_entry)
        big_dict[user_id] = todo_list

    derulo = 'todo_all_employees' + ".json"
    with open(derulo, 'w') as file:
        file.write(json.dumps(big_dict))
