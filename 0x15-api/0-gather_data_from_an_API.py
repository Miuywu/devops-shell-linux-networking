#!/usr/bin/python3
""" uses REST API to take in employee ID returns TODO list info """

# from urllib import *
import requests
from sys import argv

if __name__ == "__main__":
    strId = argv[1]# employee ID number

    user = requests.get("https://jsonplaceholder.typicode.com/users/" + strId).json()
    name = user['name']

    all_todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    totalTasks = 0
    tasksDone = 0
    for todo in all_todos:
        if str(todo['userId']) == strId:
            totalTasks += 1
            if todo['completed'] == True:
                tasksDone += 1

    first_line = 'Employee {} is done with tasks({}/{}):'.format(name,
                                                                 tasksDone,
                                                                 totalTasks)
    print(first_line)
    for todo in all_todos:
        if str(todo['userId']) == strId:
            if todo['completed'] == True:
                title = todo['title']
                print("\t" + title)

