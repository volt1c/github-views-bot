import sys
import time
import threading;
import requests

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def request_task(url, data, headers):
    requests.get(url, json=data, headers=headers)


def fire_and_forget(url, json, headers):
    threading.Thread(target=request_task, args=(url, json, headers)).start()


def increse_views(url, num, timeout):
    print()
    for i in range(num):
        fire_and_forget(url,{},{})
        sys.stdout.flush()
        print(f"{CURSOR_UP_ONE}{ERASE_LINE}Added: {i+1}/{num}")
        time.sleep(timeout/1000)


def increse_views_infinite(url, timeout):
    print()
    i = 0
    while True:
        fire_and_forget(url,{},{})
        sys.stdout.flush()
        print(f"{CURSOR_UP_ONE}{ERASE_LINE}Added: {i+1}/...")
        time.sleep(timeout/1000)
        i += 1


url = 'https://camo.githubusercontent.com/' #address of views

try:
    num = int(sys.argv[sys.argv.index("-n")+1])
except ValueError:
    num = 10
try:
    timeout = int(sys.argv[sys.argv.index("-t")+1])
except:
    timeout = 1000

print("views increaser:")
try:
    if "--infinite" in sys.argv:
        increse_views_infinite(url, timeout)
    else:
        increse_views(url, num, timeout)
except KeyboardInterrupt:
    print(f"{ERASE_LINE}>>> Exit <<<")
