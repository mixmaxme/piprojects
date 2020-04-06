import websocket

ws = websocket.create_connection("ws://localhost:8080/websocket")
print("Sending 'Hello World'...")
ws.send("Hello World")
print("Sent")
print("Receiving...")
result = ws.recv()
print("Received '%s'")
ws.close()