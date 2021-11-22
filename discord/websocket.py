import asyncio
import aiohttp
import websocket

class Websocket:
  def __init__(
    self, 
    token: str, 
    intents: int
  ):
    self.api = 'https://discord.com/api/v9'
    self.websocketurl = 'wss://gateway.discord.gg'
    self.connected = False
    self.token = token
    self.intents = intents
    self.ws = self.CreateWebsocket()
    
  def CreateWebsocket(self):
    ws = websocket.WebSocketApp(
      self.websocketurl,
      on_open = lambda ws: self.on_open(ws),
      on_message = lambda ws, msg: self.on_message(ws, msg)
    )
    return ws
