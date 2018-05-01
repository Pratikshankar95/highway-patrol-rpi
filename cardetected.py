import serial
import picamera
import time
import requests

ser=serial.Serial('/dev/ttyACM0', 9600)
camera=picamera.PiCamera()
img_dir = 'car_capture/'
server_url = "http://192.168.43.16:3000/tol2/uploadImage"

print('Car detector started')
camera.resolution = (2592, 1994)
camera.framerate = 15
camera.rotation = 180
camera.start_preview(fullscreen=False, window=(100,100,256,256))
while True:
    val=ser.readline()
    if int(val)==1:
        print('car detected')
        file_name = img_dir + 'car - ' + str(int(time.time())) + '.jpg'
        camera.capture(file_name)
        print('Image saved: ' + file_name)
        with open(file_name, 'rb') as f:
            r = requests.post(server_url, files={'car': f})
