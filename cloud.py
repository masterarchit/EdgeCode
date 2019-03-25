import serial
import json
import requests
try:
	import urllib.request as urllib2
except ImportError:
	import urllib2
from binascii import hexlify
import time
ser = serial.Serial()
ser.port = "COM5"
ser.baudrate = 9600
ser.open();

#led = "fa f5 07 f1 01 ff 00 00 f8 0d 0a"
#led = "\xfa\xf5\x07\xf1\x01\xff\x00\x00\xf8\x0d\x0a"
#sensor = "fa f5 04 f3 01 f8 0d 0a"
#sensor = "\xfa\xf5\x04\xf3\x01\xf8\x0d\x0a"

######################################

url = "http://shivangdave.com/service/index.php/feeds/second"

###################################################################
def send(timestamp,humidity,temp,currentTemp,setTemp,status):
    data = {'timestamp': timestamp, 'humidity': humidity, 'temp': temp, 'currentTemp': currentTemp, 'setTemp': setTemp, 'status': status}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    #print(data_json)
    response = requests.post(url, data=data_json, headers=headers)
####################################################
#def web_color():
#web_color = json.load(urllib2.urlopen("http://shivangdave.com/service/index.php/feeds/fourth"))[0]["color"]

####################################################
#send('2017-10-01', '1', '1', '1', '3','blue')
#######################################



######################################
if ser.isOpen():
	print(ser.port + " is open.\n")
else:
	print("No port is open.\n")

led_blue = "\xfa\xf5\x07\xf1\x01\x00\x00\xff\xf8\x0d\x0a"
led_red = "\xfa\xf5\x07\xf1\x01\xff\x00\x00\xf8\x0d\x0a"
led_green = "\xfa\xf5\x07\xf1\x01\x00\xff\x00\xf8\x0d\x0a"
sensor_byte = "\xfa\xf5\x04\xf3\x01\xf8\x0d\x0a"

color_g = "Green"
color_r = "Red"
color_b = "Blue"

while True:
    try:
    #sending data from master to slave modules.
   	#ser.write(sensor_byte)  
	#time.sleep(1)
	#print("trying to receive.")
	#now read will receive the data from sensor
	#print("Before Read.")
	#rec = ser.read(11)
	#print("After Read.")
	#since 'h' is string, trying to access it's elements with array.
	print("\nRunning.")
	web_color = json.load(urllib2.urlopen("http://shivangdave.com/service/index.php/feeds/fourth"))[0]["color"]
	if (web_color == "Red"):
		ser.write(led_red)
		led_value = color_r
	elif(web_color == "Green"):
		ser.write(led_green)
		led_value = color_g
	elif(web_color == "Blue"):
		ser.write(led_blue)
		led_value = color_b
    	#break
    except KeyboardInterrupt:
        print("\nUser interrupt encountered. Exiting...")
        time.sleep(1)
        exit()
    #except:
        # for all other kinds of error, but not specifying which one
       # print("Unknown error...")
        #time.sleep(1)
       # exit()