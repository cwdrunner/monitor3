#!/usr/bin/env python

# wifi.py

from splinter.browser import Browser
from time import sleep

URL = 'http://192.168.1.1/user_login.asp'
#URL = 'http://192.168.1.165:8082'
NAME = 'admin'
PASSWORD = '280dc932'


def main():
    executable_path = {'executable_path':'/usr/lib/chromium-browser/chromedriver'}
    br = Browser('chrome',**executable_path)
    br.visit(URL)
    sleep(5)
    if br.is_text_present('Password', wait_time=7):
        br.fill('userpass', PASSWORD)
        br.find_by_css('#LoginButton').first.click()
    sleep(5)
    if br.is_text_present('Connect', wait_time=7):
        br.find_by_id('#netmode_mode').first.click()
    sleep(5)
#############################################################################

if __name__ == "__main__":
    main()
