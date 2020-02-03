#!/usr/bin/python3
""" uses REST API to take in employee ID returns TODO list info """

#from urllib import *
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    name = https://jsonplaceholder.typicode.com/users

    first_line = 'Employee {} is done with tasks({}/{}):'.format(name,
                                                                 tasksDone,
                                                                 total_tasks)
    print(first_line)
