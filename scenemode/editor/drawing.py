import json
from itertools import cycle

from utils.settings import *


class DrawingMode:

    def __init__(self):
        tiles_list = []
        with open(TILES_FILENAME, 'r', encoding='utf8') as file:
            content = file.read()
            tiles = json.loads(content)
            for tile in tiles:
                tiles_list.append({
                    'id': tile['id'],
                    'name': tile['name'],
                    'image': tile['image']
                })

        self.tiles = cycle(tiles_list)

        self.selected_tile = next(self.tiles)

    def update(self, camera):
        pass

    def draw(self, screen):
        pass

    def action_change_selected_case(self):
        self.selected_tile = next(self.tiles)
