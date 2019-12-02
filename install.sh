# Install script for Verizon network monitor

cp monitor3.py /usr/bin/monitor3.py
cp wifi.py /usr/bin/wifi.py

sudo systemctl daemon-reload
sudo systemctl enable monitor3.service
sudo systemctl start monitor3.service
sudo systemctl status monitor3.service
