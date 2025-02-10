#!/usr/bin/env -S uv run 



from granian.server import Granian
from granian.constants import HTTPModes, Interfaces, Loops, ThreadModes


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': bytes( b'*'*5120),
    })
    
    
if __name__ == "__main__":
    server = Granian(target="main:app",interface=Interfaces.ASGI, address="0.0.0.0", port=8000, workers=1)
    server.serve()
