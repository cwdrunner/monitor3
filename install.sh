# Install script for Verizon network monitor
set -x

cp monitor.py /usr/bin/monitor.py
cp wifi.py /usr/bin/wifi.py
cp monitor.service /lib/systemd/system/monitor.service

sudo systemctl daemon-reload
sudo systemctl enable monitor.service
sudo systemctl start monitor.service
sudo systemctl status monitor.service
