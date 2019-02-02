#!/usr/bin/env python

# monitor_wifi.py
import os
import psutil
import urllib3
import subprocess

from time import sleep
from datetime import datetime

PROCNAME = 'firefoxdriver'
SLEEP_TIME = 1 * 60


def kill_firefoxdriver():
    print('# killing firefoxdriver')
    for proc in psutil.process_iter():
        if proc.name == PROCNAME:
            print('# Found firefoxdriver')
            proc.kill()


def start_wifi():
    print('# restarting wifi ({now})'.format(now=datetime.now()))
    #   os.chdir('/home/jabba/bin.python')
    process = subprocess.Popen("wifi.py", shell=True, stdout=subprocess.PIPE)


def is_internet_on(method=2):
    """Check if the Internet connection is on."""

    if method == 2:
        # http://stackoverflow.com/questions/3764291/checking-network-connection
        try:
            http = urllib3.PoolManager()
            http.request('GET', 'http://www.google.com', timeout=1, retries=False)
            return True
        except urllib3.exceptions.NewConnectionError:
            return False
    else:
        print('# warning: unknown method in is_internet_on()')


def main():
    while True:
        if not is_internet_on():
            print('# network is down')
            kill_firefoxdriver()
            start_wifi()
            kill_firefoxdriver()
        else:
            print('# network is up')
            pass

        print('# sleeping...')
        sleep(SLEEP_TIME)


#############################################################################

if __name__ == "__main__":
    main()