#!/usr/bin/env -S uv run 

from socketify import App
import asyncio
import time


class Config:
    config:bytes = None
    
    
async def get_config (res,req):
        res.end (Config.config)
    

async def wait_handle (res,req):
    sleep_time = float(req.get_parameter(0)) 
    print ("sleep time: ", sleep_time)
    await asyncio.sleep (sleep_time)
    print ("sleep time: ", sleep_time, "done")
    res.end (f"sleep: {sleep_time}")

def swait_handle (res,req):
    sleep_time = int(req.get_parameter(0)) 
    print ("ssleep time: ", sleep_time)
    time.sleep (sleep_time)
    print ("ssleep time: ", sleep_time, "done")
    res.end (f"sleep: {sleep_time}")


async def bytes_handle (res,req):
    res.end (bytes(b'x'*5120))

if __name__ == "__main__":
    with open ("config.json","rb") as f:
        Config.config = f.read()
        print ("len = ", len(Config.config))
        
    app = App()
    app.get("/wait/:time", wait_handle)
    app.get("/swait/:time", wait_handle)
    app.get("/", bytes_handle)
    app.get("/config", get_config)
    app.listen(8000, lambda config: print(f"Config: {config}"))
    app.run()
