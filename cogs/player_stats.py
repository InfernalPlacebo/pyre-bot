import json
import re
from configparser import ConfigParser
from pathlib import Path

players = []
dict = {}


class Player:
    def __init__(self, player_id, start_time, stagenum):
        self.id = player_id
        self.time = start_time
        self.stagescleared = stagenum


config_object = ConfigParser()
config_file = Path.cwd().joinpath('config', 'config.ini')
config_object.read(config_file)
ror2 = config_object["RoR2"]
general = config_object["General"]
server_address = config_object.get(
    'RoR2', 'server_address'), config_object.getint('RoR2', 'server_port')

db = Path.cwd().joinpath('data.json')


async def load_json():
    global dict
    try:
        with open('data.json', 'r') as f:
<<<<<<< HEAD
            dataDict = json.load(f)
            print('dataDict: ' + str(dataDict))  # DEBUG
    except:
=======
            dict = json.load(f)
    except Exception:
>>>>>>> parent of fd7fc95... Yeah fuck it no globals
        print('No JSON file')


async def add_player(player_id, time, stagenum):
    global players
    players.append(Player(player_id, time, stagenum))


async def update_json(player_id):
<<<<<<< HEAD
    global dataDict
    global players
=======
    global dict
>>>>>>> parent of fd7fc95... Yeah fuck it no globals
    for player in players:
        if player.id == player_id:
            player_dict = dict[player.id]
            player_dict['time'] += player.time
<<<<<<< HEAD
            player_dict['stagenum'] += player.stagescleared
            dataDict[player.id] = player_dict
=======
            dict[player.id] = player_dict
>>>>>>> parent of fd7fc95... Yeah fuck it no globals
            players.remove(player)
            with open('data.json', 'w') as f:
                json.dump(dict, f, indent=4)
            await load_json()


async def player_leave(player_id, time, stagenum):
    global players
    for player in players:
        if player.id == player_id:
            player.time = time - player.time
            player.stagescleared = stagenum - player.stagescleared
            await update_json(player.id)
        else:
            print("Doesn't match")
