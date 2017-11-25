import json

from utils import Camera
from pygame import Rect
from utils import TileCache

from layers import TerrainGroup, Terrain
from scene.eventhandler import PlaySceneEventHandler
from utils.settings import *


class PlayScene:

    def __init__(self, width, height, matrix_level):
        """
        Instanciate the raw_level
        :param width: int
        :param height: int
        :param matrix_level: [[int, int, ...], [int, int, ...], ...]
        :return EditorScene
        """
        self.tile_width = TILE_WIDTH
        self.tile_height = TILE_HEIGHT
        self.tiles_filename = TILES_FILENAME
        self.case_length_width = width
        self.case_length_height = height
        self.offset_x = 0
        self.offset_y = 0
        self.matrix_level = matrix_level
        self.tile_cache = TileCache()
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.event_handler = PlaySceneEventHandler()
        self.terrain_group = self.load_terrain_group()

    @classmethod
    def from_matrix_level(cls, matrix_level):
        """
        Instanciate the raw_level
        The sub list must all have the same size
        :param matrix_level: [[int, int, ...], [int, int, ...], ...]
        :return: Level
        """
        if not isinstance(matrix_level, list):
            raise TypeError('raw_level is not a list')
        if len(matrix_level) == 0:
            raise ValueError('raw_level is empty')
        if not isinstance(matrix_level[0], list):
            raise TypeError('raw_level elements are not list')

        height = len(matrix_level)
        width = len(matrix_level[0])
        for line in matrix_level:
            if width != len(line):
                raise ValueError('raw_level has not the same size on each line')

        return cls(width, height, matrix_level)

    @classmethod
    def from_scene_name(cls, scene_name):
        """
        Instanciate the scene from a json file
        :param scene_name: str
        :return: EditorScene
        """
        filename = '{}/{}.json'.format(FOLDER_EDITOR_SCENE, scene_name)
        with open(filename, 'r', encoding='utf8') as file:
            content = file.read()
            raw_level = json.loads(content)

        return cls.from_matrix_level(raw_level)

    def load_terrain_group(self):
        """
        Load all the json file tiles as Terrain(Sprite)
        And return them as a SpriteGroup -> TerrainGroup
        :return TerrainGroup
        """
        raw_tiles = {}
        list_tiles = []
        with open(self.tiles_filename, 'r', encoding='utf8') as file:
            content = file.read()
            tiles = json.loads(content)
            for tile in tiles:
                raw_tiles[tile['id']] = {
                    'name': tile['name'],
                    'image': tile['image']
                }

        for y, line in enumerate(self.matrix_level):
            for x, case in enumerate(line):
                rect = Rect(x * self.tile_width + self.offset_x, y * self.tile_height + self.offset_y, self.tile_width, self.tile_height)
                sprite = Terrain(rect, self.tile_cache.get_image(raw_tiles[case]['image']))
                list_tiles.append(sprite)

        return TerrainGroup(list_tiles)

    def check_events(self, events):
        """
        Check the events to execute actions
        :param events: dict events containing their duration
        """
        self.offset_x, self.offset_y = self.camera.check_events(events)
        self.event_handler(self, events)

    def update_and_draw(self, screen):
        """
        Update & draw on the screen all Sprites
        :param screen: Screen
        """
        self.terrain_group.update(self.camera)
        self.terrain_group.draw(screen)
