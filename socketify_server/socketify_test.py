#!/usr/bin/env -S uv run 

from socketify import App


async def bytes_handle (res,req):
    res.end (bytes(b'x'*5120))

if __name__ == "__main__":

    app = App()
    app.get("/", bytes_handle)
    app.listen(8000, lambda config: print(f"Config: {config}"))
    app.run()
