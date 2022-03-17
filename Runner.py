import mqttPublisher

topic01 = "udea/pi2/luz"
topic02 = "udea/pi2/luz/color"


client = mqttPublisher.connect_mqtt()

while True:
time.sleep(1)
a_enviar = input("Acción a ejecutar: \n 1.On LED \n 2.Off LED \n 3.Verde \n 4.Azul \n 5.Blanco")
msg = f"messages: {a_enviar}"

if a_enviar == "1" or a_enviar == "2":
    result = client.publish(topic01, msg)
else:
    result = client.publish(topic02, msg)
    
# result: [0, 1]
status = result[0]
if status == 0:
    print(f"Send `{msg}` to topic `{topic}`")
else:
    print(f"Failed to send message to topic {topic}")

client.loop()


