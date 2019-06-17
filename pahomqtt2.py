import paho.mqtt.client as mqtt
broker_address="192.168.1.10"

client = mqtt.Client("P1")
client.connect(broker_address)
client.subscribe("patient")

