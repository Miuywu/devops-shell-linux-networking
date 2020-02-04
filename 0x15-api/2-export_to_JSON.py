#!/usr/bin/python3
""" uses REST API to take in employee ID returns TODO list info """

import json
import requests
from sys import argv

if __name__ == "__main__":
    strId = argv[1]
    rURL = "https://jsonplaceholder.typicode.com/users/"
    user = requests.get(rURL + strId).json()
    userName = user.get('username')

    rURL2 = "https://jsonplaceholder.typicode.com/todos"
    all_todos = requests.get(rURL2).json()

    todo_list = []
    for todo in all_todos:
        list_entry = {}
        if str(todo.get('userId')) == strId:
            taskStatus = todo.get('completed')
            title = todo.get('title')
            list_entry["task"] = title
            list_entry["completed"] = taskStatus
            list_entry["username"] = userName
            todo_list.append(list_entry)

    employeeDict = {strId: todo_list}
    derulo = strId + ".json"
    with open(derulo, 'w') as file:
        file.write(json.dumps(employeeDict))
