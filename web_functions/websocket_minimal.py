import websocket

ws = websocket.create_connection("http://wordclock:1234")
print("Sending 'Hello World'...")
ws.send("Hello World")
print("Sent")
print("Receiving...")
result = ws.recv()
print("Received '%s'")
ws.close()