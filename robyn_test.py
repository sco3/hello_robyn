#!/usr/bin/env -S uv run

from robyn import Robyn
from robyn.argument_parser import Config

cfg=Config()
cfg.log_level = "WARN"
cfg.workers = 1
app = Robyn(__file__,cfg)

@app.get("/")
async def h(request):
    #return "Hello, world!\n"
    return '*' * 5120

app.start(port=8000)
