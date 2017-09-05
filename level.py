import json
from pygame import Rect
from terrain import TerrainGroup, Terrain
from tilecache import TileCache


class Level:
    tiles_filename = 'tiles/tiles.json'
    tile_width = 30
    tile_height = 30

    def __init__(self, width, height, raw_level):
        """
        Instanciate the raw_level
        :param width: int
        :param height: int
        :param raw_level: [[int, int, ...], [int, int, ...], ...]
        :return Level
        """
        self.width = width
        self.height = height
        self.raw_level = raw_level
        self.tile_cache = TileCache()
        self.terrain_group = TerrainGroup(self.load_terrain_group())

    @classmethod
    def from_raw_level(cls, raw_level):
        """
        Instanciate the raw_level
        The sub list must all have the same size
        :param raw_level: [[int, int, ...], [int, int, ...], ...]
        :return: Level
        """
        if not isinstance(raw_level, list):
            raise TypeError('raw_level is not a list')
        if len(raw_level) == 0:
            raise ValueError('raw_level is empty')
        if not isinstance(raw_level[0], list):
            raise TypeError('raw_level elements are not list')

        height = len(raw_level)
        width = len(raw_level[0])
        for line in raw_level:
            if width != len(line):
                raise ValueError('raw_level has not the same size on each line')

        return cls(width, height, raw_level)

    @classmethod
    def from_json_file(cls, filename):
        """
        Instanciate the raw_level from a json file
        :param filename: str json filename
        :return: Level
        """
        with open(filename, 'r', encoding='utf8') as file:
            content = file.read()
            raw_level = json.loads(content)

        return cls.from_raw_level(raw_level)

    def load_terrain_group(self):
        """
        Load all the json file tiles as Terrain(Sprite)
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

        for y, line in enumerate(self.raw_level):
            for x, case in enumerate(line):
                rect = Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height)
                sprite = Terrain(rect, self.tile_cache.get_image(raw_tiles[case]['image']))
                list_tiles.append(sprite)

        return list_tiles

    def add_case(self, pos):
        """

        :param pos:
        :return:
        """
        x, y = pos
        x = (x // self.tile_width) * self.tile_width
        y = (y // self.tile_height) * self.tile_height
        rect = Rect(x, y, self.tile_width, self.tile_height)
        sprite = Terrain(rect, self.tile_cache.get_image('tiles/plaine.png'))
        self.terrain_group.add(sprite)

