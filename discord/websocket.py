import asyncio
import websocket
import json

class Websocket:
  def __init__(
    token: str,
    intents: int,
    loop: asyncio.AbstractEventLoop
  ):
    self.version = 9
    self.token = token
    self.websocketurl = 'wss://gateway.discord.gg'
    self.api = 'https://discord.com/api/v{}'.format(self.version)
    self.headers = {
      'Authorization': 'Bot ' + self.token
    }
    self.heartbeat = {
      'op': 1,
      'd': 2
    }
    self.dx = {
      'op': 2,
      'd': {
        'token': self.token,
        'intents' self.intents,
        'properties': {
          '$os': 'linux',
          '$browser': 'disco',
          '$device': 'disco'
        }
      }
    }
    self.websocket = self.CreateWebSocket()
  
  def CreateWebSocket(self):
    ws = websocket.WebSocketApp(
      self.websocketurl,
      on_open = lambda ws: self.on_open(ws),
      on_message = lambda ws, msg: self.on_message(ws, msg)
    )
    return ws
  
  def on_open(self, ws):
    self.send(self.dx)

  def on_message(self, ws, msg):
    msg = json.loads(msg)
