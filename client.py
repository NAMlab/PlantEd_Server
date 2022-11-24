import asyncio
import websockets
import json

def render(gametime, game_status, plant, environment):
  print("Rendering (gametime = " + str(gametime) + ")")
  # Render everything

async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
      print("Beginning game...")
      action1 = {
          'delta_t': 1,
          'player_inputs': {
              'growth_percentages': {'root': 1, 'stem': 0, 'leaf': 0, 'starch': 0}            # more stuff (like root growth, leaves...)
            },
          'actions': ['test']
          }
      print("Sending first tick:")
      print(json.dumps(action1, indent=2))
      await websocket.send(json.dumps(action1))
      print("Response:")
      response = await websocket.recv()
      print(response)
      render(**json.loads(response))

      await asyncio.sleep(2)

      action2 = {
          'delta_t': 40, # of course this would be calculated from the last update
          'player_inputs': {
            'growth_percentages': {'root': 30, 'stem': 10, 'leaf': 10, 'starch': 50}
            },
          'actions': ['test']
          }
      print("Sending second tick:")
      print(json.dumps(action2, indent=2))
      await websocket.send(json.dumps(action2))
      print("Response:")
      response = await websocket.recv()
      print(response)
      render(**json.loads(response))

      await asyncio.sleep(2)

      action3 = {
          'delta_t': 3000, # of course this would be calculated from the last update
          'player_inputs': {
              'growth_percentages': {'root': 100, 'stem': 0, 'leaf': 0, 'starch': 0}
          },
          'actions': ['test']
          }
      print("Sending 3rd tick:")
      print(json.dumps(action3, indent=2))
      await websocket.send(json.dumps(action3))
      print("Response:")
      response = await websocket.recv()
      print(response)
      render(**json.loads(response))

asyncio.run(main())
