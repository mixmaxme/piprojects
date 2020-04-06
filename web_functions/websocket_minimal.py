import socketio

sio = socketio.Client()

sio.connect('http://localhost:1234')
print("Shabs konnetn")
