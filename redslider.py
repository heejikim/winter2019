import cayenne.client
from gpiozero import PWMLED
led1=PWMLED(23)
led2=PWMLED(24)
led3=PWMLED(22)

MQTT_USERNAME = "90f3b8b0-45f0-11e9-b67a-4730a9bffc37"
MQTT_PASSWORD = "8b738715618d09cc6174d4753fe86eb41b919d22"
MQTT_CLIENT_ID = "f1ecf030-45f2-11e9-ba40-5d168a516101"

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