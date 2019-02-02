Python3 version of util to monitor network and login to MIFI to reset it.

Commands to Makes this work

Python 3

Pip3 commands to install libraries

which python
 
   11  python3 -V
 
   13  pip3 install psutil
   14  pip3 install urllib3
   15  pip3 install splinter
 
cd to downloads
   25  sudo dpkg -i chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb
 
   33  sudo apt-get install chromium-chromedriver
 
   35  dpkg -L chromium-chromedriver
 
Driver path is in wifi.py file. Can also be added to $PATH
