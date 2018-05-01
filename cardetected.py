import serial
import picamera
import time
import requests

ser=serial.Serial('/dev/ttyACM0', 9600)
camera=picamera.PiCamera()
img_dir = 'car_capture/'
server_url = "http://192.168.43.16:3000/tol1/uploadImage"

while True:
    val=ser.readline()
    if int(val)==1:
        print('car detected')
        file_name = img_dir + 'car - ' + str(int(time.time())) + '.jpg'
        camera.capture(file_name)
        with open(file_name, 'rb') as f:
            r = requests.post(server_url, files={'car': f})
