import os
import time
import paho.mqtt.client as mqtt

import subprocess
from subprocess import call

broker_IP = "192.168.1.10"
broker_Port = 1883 #Default Port

#Bedsite Unit ID  string 
patientID = "200"

# ps aux | grep twinkle
# sudo kill -1 xxxx


#How to write to anoter terminal
#os.system("twinkle --call 101")

print ("Bedsiteunit-Running\nBedsiteID: " + patientID)

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))
    client.subscribe("patient")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    
    message = str(msg.payload)
    print("MQTT Msg:" + message)
    split_message = message.split(':')

    # This bedsite unit get request from MQTT Message
    if(split_message[0] == patientID):
        if (split_message[1][0:4] == "call"):
            phonenumber = split_message[1].split(' ')
            os.system("twinkle --call " +  phonenumber[1] ) 
        elif (split_message[1] == "answer"):
            os.system("twinkle --cmd answer")
        elif (split_message[1] == "bye"):
            os.system("twinkle --cmd bye")
        else:
            print("Invalid MQTT Incomming message")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_IP, broker_Port, 60)

client.loop_forever()



