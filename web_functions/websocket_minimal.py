#!/usr/bin/python

import json 
import socketio
import board
import neopixel

# Define global values
# define clock
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))

# get socket
sio = socketio.Client()

# set variables
i = 0

# build list for rearrangements
rearrange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
for j in range(2,9):
    for i in range((18*(j-1)*2),(18*(j-1)*2)-18,-1):
        rearrange = rearrange + [i]
    for i in range((18*(j-1)*2)+1,(18*(j-1)*2)+19):
        rearrange = rearrange + [i]
for i in range(288,270,-1):
    rearrange = rearrange + [i]

# make the json_body magic
json_list = []
json_data_example = '{"pixel_id": 1, "pixel_r": 255, "pixel_g": 255, "pixel_b": 255, "pixel_a": 1}'

class ImportJson(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

def addpixel():
    global i
    pixels[i] = (255,0,0)
    i = i + 1

@sio.on('s_changePixel')
def on_message(json_data):
    # Load json body
    print("Bin im Script")
    print(json_data)
    #parsed_json = json.loads(json_data)
    #parsed_json = ImportJson(json_data)
    #print(parsed_json)

    # Iterate through every line in the json body
    for line in json_data:
        if json_data['pixelR'] and json_data['pixelG'] and json_data['pixelB']:
            # import color and check brightness
            r = int(int(json_data['pixelR'])*float(json_data['pixelA']))
            if r > 255:
                r = 255
            g = int(int(json_data['pixelG'])*float(json_data['pixelA']))
            if g > 255:
                g = 255
            b = int(int(json_data['pixelB'])*float(json_data['pixelA']))
            if b > 255:
                b = 255
        else:
            continue

        if json_data['pixelId']: # if ID is not empty
            j = int(rearrange[int(json_data['pixelId'])])-1
            pixels[j] = (r, g, b)
        elif json_data['pixelCol']:
            if json_data['pixelRow']:
                value = (18*(json_data['pixelRow'] - 1) + json_data['pixelCol'])
                j = int(rearrange[value])
                pixels[j] = (r, g, b)
        else:
            continue




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