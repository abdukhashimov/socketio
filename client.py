import asyncio
import socketio


# asyncio
sio = socketio.Client()


@sio.event
def message(data):
    print('I received a message!')
    print(data)
    message_ = input('> ')
    sio.emit('message', message_)

@sio.event
def connect():
    print("I'm connected!")


@sio.event
def connect_error():
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")


sio.connect('http://localhost:8080')
sio.emit('message', 'I have joined')

