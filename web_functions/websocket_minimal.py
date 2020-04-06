#!/usr/bin/python
 
import socketio
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))

sio = socketio.Client()
global i 
i = 0


@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    pixels[i] = (255,0,0)
    i = i + 1

@sio.on('newMessage')  
def on_message(data):
    print("Habs auch gemerkt")
    pixels[1] = (255,0,0)
    #i = i + 1

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:1234')


print("Shabs konnetn")
