import paho.mqtt.client as mqtt
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    
client = mqtt.Client()
client.on_connect = on_connect
client.connect("192.168.1.109", 1883, 60)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    formatted_temp = "{:.2f}".format(temperature)
    formatted_hum = "{:.2f}".format(humidity)
    
    # the four parameters are topic, sending content, QoS and whether retaining the message respectively
    client.publish('myhome/sensor1', payload=formatted_temp, qos=0, retain=False)
    client.publish('myhome/sensor2', payload=formatted_hum, qos=0, retain=False)
    print(f"send {formatted_temp} to myhome/sensor1")
    print(f"send {formatted_hum} to myhome/sensor2")
    time.sleep(1)
client.loop_forever()
