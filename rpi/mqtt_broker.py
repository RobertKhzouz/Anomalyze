import paho.mqtt.client as mqtt

import base64
import json

topic = 'anomalyze/data' #Topic for MQTT broker

def configure():
	def on_connect(mosq, obj, rc):
		print('Connected')
	
	def on_publish(client, userdata, mid):
		print('Data published')
	
	host = '35.23.168.227'
	port = 1883
	
	client = mqtt.Client()
	client.on_publish, client.on_connect = on_publish, on_connect
	
	client.connect(host, port, 60)
	
	return client


#Encode image in base64
def encode_image(img_file):
	with open(img_file, 'rb') as img:
		return base64.b64encode(img.read()).decode('utf-8')


def send_data(sen, img):
	#Establish MQTT connection
	client = configure()
	
	#Combine sensor tuple and encoded image into one message
	data = json.dumps({
		"sensor": {
			"temperature": sen[0],
			"pressure": sen[1]
		},
		"image": img
		})
	
	#Send message to subsciber on backend server
	client.publish(topic, data)
	
	#Safely disconnect
	client.disconnect()
