import mqtt_broker as mqtt

import cv2

import serial

from time import sleep, localtime, strftime

ser = serial.Serial('/dev/ttyUSB0', 9600)

#Initialize camera
cam = cv2.VideoCapture(0)

while True:
	#I2C Communication
	data = ser.readline().decode('utf-8').rstrip()
	parts = data.split(',')
	temperature = float(parts[0])
	humidity = float(parts[1])
	
	#Convert sensor data to json string for delivery
	bme_read = (temperature, humidity)
	
	#USB Camera operations
	result, image = cam.read()
	
	if result:
		#Generate image
		img_name = f"{strftime('%Y_%m_%d_%H_%M_%S', localtime())}.jpg"
		cv2.imwrite(img_name, image)
		
		#Encode image for delivery
		encode_img = mqtt.encode_image(img_name)
	else:
		print('Camera not recognized')
		
	mqtt.send_data(bme_read, encode_img)
		
	#Pause to ensure ability for system to read data
	sleep(1)
