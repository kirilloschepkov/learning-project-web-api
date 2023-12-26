from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from routes.manager import manager

router_websocket = APIRouter()


@router_websocket.websocket("/ws/{name}")
async def websocket_endpoint(websocket: WebSocket, name: str):
    await manager.connect(websocket)
    await manager.broadcast(f"{name} присоединился в чат")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{name}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{name} покинул чат")
