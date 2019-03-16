import cayenne.client
from gpiozero import PWMLED
led1=PWMLED(23)
led2=PWMLED(24)
led3=PWMLED(22)

MQTT_USERNAME = "INSERT MQTT_USERNAME HERE"
MQTT_PASSWORD = "INSERT MQTT_PASSWORD HERE"
MQTT_CLIENT_ID = "INSERT MQTT_CLIENT_ID HERE"

def on_message(message):
    print("message received:" + str(message))
    if message.channel==2:
        led1.value=float(message.value)/255
        
    if message.channel==3:
        led2.value=float(message.value)/255
        
    if message.channel==4:
        led3.value=float(message.value)/255
        
client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:
    client.loop()
