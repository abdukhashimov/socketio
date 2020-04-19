from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
def connect(sid, environ):
    print("connect ", sid)



@sio.on('message')
async def print_message(sid, message):
    print("Socket ID: ", sid)
    print(message)
    # await a successful emit of our reversed message
    # back to the client
    reply = input('> ')
    await sio.emit('message', reply)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
