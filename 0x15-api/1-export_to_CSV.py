#!/usr/bin/python3
""" uses REST API to take in employee ID returns TODO list info """

import csv
import requests
from sys import argv

if __name__ == "__main__":
    strId = argv[1]
    rURL = "https://jsonplaceholder.typicode.com/users/"
    user = requests.get(rURL + strId).json()
    userName = user.get('username')

    rURL2 = "https://jsonplaceholder.typicode.com/todos"
    all_todos = requests.get(rURL2).json()

    csvFile = strId + ".csv"
    with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,)
        for todo in all_todos:
            if str(todo.get('userId')) == strId:
                taskStatus = str(todo.get('completed'))
                title = todo.get('title')
                writer.writerow([strId, userName, taskStatus, title])
