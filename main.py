# file: a_simple_sub.py

from mqtt import MQTTClient
import pycom
import sys
import time
import ufun

wifi_ssid = "AndroidAP"
wifi_passwd = "stalin1986"
broker_addr = "192.168.43.113"
#MYDEVID = "iot_10"

dev_id = 'test'

def settimeout(duration):
   pass

def on_message(topic, msg):
    print("Received msg: ", str(msg), "with topic: ", str(topic))

### if __name__ == "__main__":

ufun.connect_to_wifi(wifi_ssid, wifi_passwd)

client = MQTTClient(dev_id, broker_addr, 1883)
client.set_callback(on_message)

print ("Connecting to broker: " + broker_addr)
try:
	client.connect()
except OSError:
	print ("Cannot connect to broker: " + broker_addr)
	sys.exit()
print ("Connected to broker: " + broker_addr)

client.subscribe('iot_10/battery/#')

print('Waiting messages...')
while 1:
    client.check_msg()
