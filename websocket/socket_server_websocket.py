import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f'message received: {message}')
        await websocket.send(f'your message was: {message}')

async def main():
    async with websockets.serve(echo, "192.168.31.176", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())