# Usage: python server.py <level>
import asyncio
import websockets
import json
from game import Game
import cobra
from helpers import create_objective, update_objective


def load_level(level_name):
    global game_status, game
    game = Game()
    print("Loading level '" + level_name + "'")
    # Load environment, weather etc.
    game_status = 'running'


def get_environment():
    environment = {
        'sunlight': 0.5,
        'humidity': 0.3,
        'temperature': 24.5,
        'soil_water': [
            [0, 0.1, 2.4, 0.4, 0],
            [0, 1.2, 4.4, 0.8, 0],
            [0, 0.1, 2.1, 0.1, 0],
            [0, 0.0, 1.3, 0.2, 0],
        ]
        # more paramters...
    }
    return (environment)


def get_plant():
    global game
    return game.plant.get_plant()


def update(delta_t, player_inputs, actions):
    global game_status, game
    print("Simulating next " + str(delta_t) + "s gametime")
    # Update Plant, Environment, Water grid etc.
    game.update(delta_t, player_inputs, actions)
    total_plant_mass = game.plant.get_total_plant_mass()
    if total_plant_mass > 20:
        game_status = 'won'
    elif total_plant_mass == 0:
        game_status = 'lost'

async def respond(websocket):
    global game_status, game
    async for message in websocket:
        update(**json.loads(message))

        response = {
            'gametime': game.gametime.get_time(),
            'game_status': game_status,
            'plant': game.plant.get_plant(),
            'environment': get_environment()
        }
        await websocket.send(json.dumps(response, indent=2))


async def main():
    async with websockets.serve(respond, "localhost", 8765):
        await asyncio.Future()  # run forever


load_level('Gatersleben')
asyncio.run(main())
