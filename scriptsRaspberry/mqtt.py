#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# All rights reserved.

# This shows a simple example of an MQTT subscriber using a per-subscription message handler.

# import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.client as mqtt
import json
import RPi.GPIO as GPIO

#CONFIGURACIÓN LEDS
import time

GPIO.setwarnings(False)

white = 13
blue = 15
green = 11

lastColor = white

GPIO.setmode(GPIO.BOARD)
GPIO.setup(white, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def whiteOn():
    lastColor = white
    cleanAll()
    GPIO.output(white, True)
    GPIO.output(blue, True)
    GPIO.output(green, True)

def blueOn():
    lastColor = blue
    cleanAll()
    GPIO.output(blue, True)

def greenOn():
    lastColor = green
    cleanAll()
    GPIO.output(green, True)

def cleanAll():
    GPIO.output(white, False)
    GPIO.output(blue, False)
    GPIO.output(green, False)

def powerOn():
    #if lastColor == 'red':
    #    redOn()
    #elif lastColor == 'green':
    #    greenOn()
    #elif lastColor == 'blue':
    #    blueOn()
    if lastColor == white:
        whiteOn()
    elif lastColor == green:
        greenOn()
    elif lastColor == blue:
        blueOn()
    else :
        cleanAll()


def powerOff() :
    cleanAll()

#from playsound import playsound 
# from pprint import pprint

def msg_decode(msg):
    try:
        payload = json.loads(msg.payload.decode('UTF-8'))['msg']
    except:
        payload = ''
    # if 'msg' in payload:
    #     payload = payload['msg']
    # else:
    #     payload = ''
    return payload
def on_message_luz(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $udea/pi2/luz
    payload = msg_decode(msg)

    if(payload == 'prender'):
        print('encender.wav')
        print('Echo enciende la luz')
        powerOn()
    elif(payload == 'apagar'):
        print('apagar.wav')
        print('Echo apaga la luz')
        powerOff()
    else:
        print("Errror: " + msg.topic + str(msg.payload))


def on_message_color(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $udea/pi2/luz/color
    payload = msg_decode(msg)
    
    if(payload == 'verde'):
        print('verde.wav')
        print('Echo luz verde')
        greenOn()
    elif(payload == 'azul'):
        print('azul.wav')
        print('Echo luz azul')
        blueOn()
    elif(payload == 'blanco'):
        print('blanco.wav')
        print('Echo luz blanca')
        whiteOn()
    else:
        print("Errror: " + msg.topic + str(msg.payload))


def on_message(mosq, obj, msg):
    # This callback will be called for messages that we receive that do not
    # match any patterns defined in topic specific callbacks, i.e. in this case
    # those messages that do not have topics $SYS/broker/messages/# nor
    # $SYS/broker/bytes/#
    payload = msg_decode(msg)
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


mqttc = mqtt.Client()

# Add message callbacks that will only trigger on a specific subscription match.
mqttc.message_callback_add("udea/pi2/luz", on_message_luz)
mqttc.message_callback_add("udea/pi2/luz/color", on_message_color)
# mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect("broker.emqx.io", 1883, 60)
mqttc.subscribe("udea/pi2/#", 0)

mqttc.loop_forever()







# import paho.mqtt.client as mqtt

# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))

#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("udea/pi2/#")

# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))

# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message

# client.connect("broker.emqx.io", 1883, 60)

# # Blocking call that processes network traffic, dispatches callbacks and
# # handles reconnecting.
# # Other loop*() functions are available that give a threaded interface and a
# # manual interface.
# client.loop_forever()