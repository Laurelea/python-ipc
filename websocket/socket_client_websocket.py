import asyncio
import websockets

# host = 'localhost'
host = '192.168.31.176'
port = 8765

async def hello():
    async with websockets.connect(f"ws://{host}:{port}") as websocket:
        await websocket.send("Hello from client!")
        message = await websocket.recv()
        print(f'received from server: {message}')

asyncio.run(hello())