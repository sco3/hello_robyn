
from socketify import ASGI

    
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
        'body': bytes(b'x'*5120),
    })
    return

def run_app():
    ASGI(app,lifespan=False).listen(8000).run()
    
    
run_app()    
