from email import message
from pydoc import cli
import paho.mqtt.client as mqtt
import json
import os

client=mqtt.Client()
IP = os.environ.get("IP")
PORT = os.environ.get("PORT")
client.connect(IP, PORT, 60)

def on_connect(client,userdata,flags,rc):
     print('Connected with result code:'+str(rc))
     client.subscribe('iort')

def on_message(_, userdata, msg):
    data = msg.payload.decode('utf-8')
    bot1 = json.loads(data)["bot1"]
    bot2 = json.loads(data)["bot2"]
    if bot1>=bot2:
        print("Task allocated to bot2")
        client.publish("bot2", bot2)
    else:
        print("Task allocated to bot1")
        client.publish("bot1", bot1)



client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()