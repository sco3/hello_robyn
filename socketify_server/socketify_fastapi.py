
from socketify import ASGI
from fastapi import FastAPI

    
app=FastAPI()
@app.get("/")    
async def root():
    return  bytes(b'x'*5120)

def run_app():
    ASGI(app,lifespan=False).listen(8000).run()
    
    
run_app()    
