#!/bin/bash

echo "BedsiteUnit Install"

sudo apt-get update
sudo apt-get -y install twinkle
sudo apt-get -y install mosquitto-clients
pip install paho-mqtt