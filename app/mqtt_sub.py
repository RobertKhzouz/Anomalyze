import paho.mqtt.client as mqtt
import json
from decode_img import decode
from interactive_sql import Commands
import random

#Variable names to identify broker
hostname = '35.23.168.227'
broker_port = 1883
topic = 'anomalyze/data'

def on_connect(client, data, flags, rc):
    client.subscribe(topic)
    print('Connected with result code ' + str(rc))


def on_message(client, userdata, msg):
    print('Message received')
    pi_data = json.loads(msg.payload.decode())
    sensor_id = random.randint(1,10)
    temperature = pi_data['sensor']['temperature']
    pressure = pi_data['sensor']['pressure']
    # image = decode(pi_data['image'])
    Commands.insert_sensor(sensor_id=sensor_id, temperature=temperature, pressure=pressure)


def on_subscribe(client, userdata, mid, qos):
    print('Subscribed to MQTT topic')

def init_mqtt():
    #initialize instance of MQTT client
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe

    #Start up MQTT subscriber
    client.connect(hostname, broker_port, 60)
    client.subscribe(topic)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("MQTT client stopping...")