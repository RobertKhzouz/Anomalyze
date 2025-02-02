import paho.mqtt.client as mqtt

#Variable names to identify broker
hostname = '35.23.168.227'
broker_port = 1883
topic = 'anomalyze/data'

def on_connect(client, data, flags, rc):
    client.subscribe(topic)
    print('Connected with result code ' + str(rc))


def on_message(client, userdata, msg):
    print(f'Message received: {msg.payload.decode()}')
    


def on_subscribe(client, userdata, mid, qos):
    print('Subscribed to MQTT topic')


#initialize instance of MQTT client
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

#Start up MQTT subscriber
client.connect(hostname, broker_port, 60)
client.subscribe(topic)
client.loop_forever()

