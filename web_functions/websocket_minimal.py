#!/usr/bin/python
 
import socketio
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))

sio = socketio.Client()
i = 0

def addpixel():
    global i
    pixels[i] = (255,0,0)
    i = i + 1


@sio.event
def connect():
    print('connection established') 

@sio.on('newMessage')  
def on_message(data):
    addpixel()
    print("Habs auch gemerkt")

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:1234')


print("Shabs konnetn")
