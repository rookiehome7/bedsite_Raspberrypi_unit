#!/bin/bash
echo "BedsiteUnit Start install"

sudo apt-get update
sudo apt-get -y install twinkle
sudo apt-get -y install mosquitto-clients
pip install paho-mqtt
sudo nano /etc/asound.conf


Add Python Script to /home/pi/.bashrc
echo "
Start Running SIP Phone
sleep 2
while ! ping -c 1 -W 1 192.168.1.10 > /dev/null; do
	echo Wating for network
	sleep 1
	done 
python /home/pi/bedsite_Raspberrypi_unit/SIP_Handle.py &
python /home/pi/bedsite_Raspberrypi_unit/MQTT_Handle.py &
" >> /home/pi/.bashrc

# Configure Default sound
echo "
pcm.!default {
  type asym
  capture.pcm "mic"
  playback.pcm "speaker"
}
pcm.mic {
  type plug
  slave {
    pcm "hw:1,0"
  }
}
pcm.speaker {
  type plug
  slave {
    pcm "hw:0,0"
  }
}
" > /etc/asound.conf

echo "Setup Finish"