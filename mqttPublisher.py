from paho.mqtt import client as mqtt_client
import random
import time


broker = 'broker.emqx.io'
port = 1883
topic01 = "udea/pi2/luz"
topic02 = "udea/pi2/luz/color"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# The callback for when the client receives a CONNACK response from the server.

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("-->Conectado al Broker EMQX!!")
        else:
            print("-->No se pudo establecer la conexión",rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(self):
    while True:
        time.sleep(5)
        a_enviar = input("Acción a ejecutar: \n 1.On LED \n 2.Off LED \n 3.Verde \n 4.Azul \n 5.Blanco \n")
    
        if a_enviar == "1": msg = "{\"msg\" : \"prender\"}"
        elif a_enviar == "2": msg = "{\"msg\" : \"apagar\"}"
        elif a_enviar == "3": msg = "{\"msg\" : \"verde\"}"
        elif a_enviar == "4": msg = "{\"msg\" : \"azul\"}"
        elif a_enviar == "5": msg = "{\"msg\" : \"blanco\"}"
        

        if a_enviar == "1" or a_enviar == "2":
            topic = topic01
        else:
            topic = topic02

        
        result = client.publish(topic, msg)    
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send {msg} to topic {topic}")
        else:
            print(f"Failed to send message to topic {topic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()