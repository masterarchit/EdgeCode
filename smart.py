import serial
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

if ser.isOpen():
	print(ser.port + " is open.\n")
else:
	print("No port is open.\n")

led_blue = "\xfa\xf5\x07\xf1\x01\x00\x00\xff\xf8\x0d\x0a"
led_red = "\xfa\xf5\x07\xf1\x01\xff\x00\x00\xf8\x0d\x0a"
led_green = "\xfa\xf5\x07\xf1\x01\x00\xff\x00\xf8\x0d\x0a"
sensor_byte = "\xfa\xf5\x04\xf3\x01\xf8\x0d\x0a"
motor_on = "\xfa\xf5\x05\xf4\x01\x05\xff\x0d\x0a"
motor_off = "\xfa\xf5\x05\xf4\x01\x00\xfa\x0d\x0a"
color_g = "Green"
color_r = "Red"
color_b = "Blue"


while True:
    try:
    #sending data from master to slave modules.
   	ser.write(sensor_byte)  
	time.sleep(1)
	#print("trying to receive.")
	#now read will receive the data from sensor
	#print("Before Read.")
	rec = ser.read(11)
	#print("After Read.")
	#since 'h' is string, trying to access it's elements with array.
	h = hexlify(rec)
	#let's find out humidity
	a = h[8]
	b = h[9]
	hum_1 = a+b
	q = h[10]
	w = h[11]
	hum_2 = q+w
	hum = hum_1 + hum_2
	p = int(hum,16)
	new_p = float(p)
	new_p = (new_p/1000)
	#print(new_p)
	print("\nHumidity is : " + "{:.1%}".format(new_p))
	#let's find out temperature
	j = h[12]
	k = h[13]
	temp_1 = h[12]+h[13]
	l = h[14]
	m = h[15]
	temp_2 = h[14]+h[15]
	temp = temp_1+temp_2
	f = int(temp,16)
	new_f = (float(f)/10)
	print("Current Temperature is : " + str(new_f) + " Celsius")
	set_temp = 26.5
	set_hum = 0.75
	if new_p <= set_hum:
		ser.write(led_green)
		print("Turning LED to Green.")
	else:
		ser.write(led_red)
		print("Turning LED to Red.")
	if new_f <= set_temp:
		ser.write(motor_off)
		print("Turning motor to Off.")
	else:
		ser.write(motor_on)
		print("Turning motor to On.")
	#s = open('C:\Users\Archit\Desktop\Webpage\DEVELOPMENT\Doc\Logs\sensor_log.txt', 'a')
	#q = open('C:\Users\Archit\Desktop\Webpage\DEVELOPMENT\Doc\Logs\sensor_log_s.txt', 'w')

	#t_data = time.strftime('%a, %I:%M:%S on %b %d, %Y (%Z)')

	#s.write(t_data + " -- Humidity : " + "{:.1%}".format(new_p)+ " & Temperature : " +str(new_f) + " Celsius\n")
	#q.write(t_data + " -- Humidity : " + "{:.1%}".format(new_p)+ " & Temperature : " +str(new_f) + " Celsius\n")
	#s.write("Current Temperature : " + str(new_f) +" & Set Temperature : " + str(set_temp) + " --> LED: "+ str(led_value) + "\n\n")
	#q.write("Current Temperature : " + str(new_f) +" & Set Temperature : " + str(set_temp) + " --> LED: "+ str(led_value) + "\n\n")
	#s.close()
	#q.close()

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