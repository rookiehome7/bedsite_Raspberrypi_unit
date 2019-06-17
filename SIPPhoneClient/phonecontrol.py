import os
import time
import paho.mqtt.client as mqtt

broker_IP = "192.168.1.10"
broker_Port = 1883 #Default Port

# In string 
patientID = "200"

#How to write to anoter terminal
#os.system("twinkle --call 101")

print ("Bedsiteunit-Running\nBedsiteID: " + patientID)

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))
    client.subscribe("patient")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    
    message = str(msg.payload)
    print("MQTT Message:" + message)
    split_message = message.split(':')

    if(split_message[0] == patientID):
        print ("This patient incoming message")
        if (split_message[1] == "call 101"):
            os.system("twinkle --call 101")
        if (split_message[1] == "answer"):
            os.system("twinkle --cmd answer")
        if (split_message[1] == "bye"):
            os.system("twinkle --cmd bye")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_IP, broker_Port, 60)

client.loop_forever()

