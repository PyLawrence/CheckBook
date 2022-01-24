# used to update the django project when changes are made
# if using the run command, this will start the server and open the page in Chrome
# pycharm has integration with django, however it is only available in pro, so this will do.

import os
import time
import argparse
import webbrowser
import asyncio

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='runserver')
runserver = subparser.add_parser('run')
args = parser.parse_args()

COMMAND_MKMIGRATIONS = "python manage.py makemigrations"

COMMAND_MIGRATE = "python manage.py migrate"

COMMAND_RUNSERVER = "python manage.py runserver"

async def openPage(delay):
    await asyncio.sleep(delay)
    url = 'http://127.0.0.1:8000/'
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)

os.system(COMMAND_MKMIGRATIONS)
time.sleep(3)
os.system(COMMAND_MIGRATE)

async def execServer():
    await openPage(2)
    os.system(COMMAND_RUNSERVER)

if args.runserver == 'run':
    asyncio.run(execServer())
