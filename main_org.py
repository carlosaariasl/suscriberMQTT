from network import WLAN
from mqtt import MQTTClient
from machine import idle
import time
import pycom

wifi_ssid = "AndroidAP"
wifi_passwd = "stalin1986"
broker_addr = "192.168.43.113"
MYDEVID = "iot_10"


def settimeout(duration):
   pass

def on_message(topic, msg):
    print("topic is: " + str(topic))
    print("msg is: " + str(msg))

wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == wifi_ssid:
        print("Network " + wifi_ssid + " found!")
        wlan.connect(net.ssid, auth=(net.sec, wifi_passwd), timeout=5000)
        while not wlan.isconnected():
            #machine.idle() # save power while waiting
            idle() # save power while waiting
        print("WLAN connection succeeded!")
        print (wlan.ifconfig())
        break

client = MQTTClient(MYDEVID, broker_addr, 1883)
if not client.connect():
    print ("Connected to broker: " + broker_addr)

client.set_callback(on_message)
client.subscribe("battery/percentage/")

print("Checking messages ...")

while 1:
    client.check_msg()
