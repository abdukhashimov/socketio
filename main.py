from aiohttp import web

import socketio


# creating a asyncIoServer
sio = socketio.AsyncServer()


# create new aiohttp web server
app = web.Application()

sio.attach(app)


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
@sio.on('message')
async def print_message(sid, message):
    print("Socket ID: ", sid)
    print(message)
    # await a successful emit of our reversed message
    # back to the client
    await sio.emit('message', message[::-1])


# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)
