#!/usr/bin/env -S uv run

from socketify import ASGI
from blacksheep import Application, Response, Content, get


app = Application()


@get("/")
async def root(r) -> Response:
    # print (type (r))
    return Response(200, content=Content(b"text/plain", bytes(b'x'*5120)))

def run_app():
    ASGI(app,lifespan=False).listen(8000).run()
    
    
run_app()    
