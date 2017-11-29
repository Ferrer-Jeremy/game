from pygame.sprite import Group, Sprite
from utils.settings import *
import pygame
from pygame import Rect
import json


class TerrainGroup(Group):
    """
    A group of sprites representing the terrain
    At the base layer
    Every thing will drawn onto this
    """

    layer = 0

    def __init__(self, width_matrix, height_matrix, sprite_matrix, *sprites):
        super(TerrainGroup, self).__init__(*sprites)
        self.sprite_matrix = sprite_matrix
        self.width_matrix = width_matrix
        self.height_matrix = height_matrix

    @classmethod
    def load(cls, level_matrix, tile_cache):
        """
        Load all the json file tiles as Terrain(Sprite)
        And return them as a SpriteGroup -> TerrainGroup
        :return TerrainGroup
        """
        raw_tiles = {}
        height_matrix = len(level_matrix)
        width_matrix = len(level_matrix[0])
        sprite_matrix = [[None for x in range(width_matrix)] for y in range(height_matrix)]
        sprites = []

        with open(TILES_FILENAME, 'r', encoding='utf8') as file:
            content = file.read()
            tiles = json.loads(content)
            for tile in tiles:
                raw_tiles[tile['id']] = {
                    'name': tile['name'],
                    'image': tile['image']
                }

        offset_x = 0
        offset_y = 0

        for y, line in enumerate(level_matrix):
            for x, case in enumerate(line):
                rect = Rect(x * TILE_WIDTH + offset_x, y * TILE_HEIGHT + offset_y, TILE_WIDTH, TILE_HEIGHT)
                sprite = TerrainSprite(rect, tile_cache.get_image(raw_tiles[case]['image']))
                sprite_matrix[y][x] = sprite
                sprites.append(sprite)

        return cls(width_matrix, height_matrix, sprite_matrix, sprites)

    def update(self, camera):
        """call the update method of every member sprite
        Calls the update method of every member sprite. All arguments that
        were passed to this method are passed to the Sprite update function.
        """
        for s in self.sprites():
            s.update(camera)

    def action_replace_case(self, scene):
        """
        Replace at the cursor pos the case by the case_selected
        Then reload the terrain
        """
        tile = scene.drawing_scene_mode.selected_tile

        raw_cursor_x, raw_cursor_y = pygame.mouse.get_pos()
        cursor_x = raw_cursor_x - scene.camera.rect.x
        cursor_y = raw_cursor_y - scene.camera.rect.y

        # We check if the cursor is in the map
        if 0 <= cursor_x < TILE_WIDTH * self.width_matrix and 0 <= cursor_y < TILE_HEIGHT * self.height_matrix:
            case_x = cursor_x // TILE_WIDTH
            case_y = cursor_y // TILE_HEIGHT
            offset_x = scene.camera.offset_x
            offset_y = scene.camera.offset_y

            sprite_to_change = self.sprite_matrix[case_y][case_x]
            sprite_to_change.rect = Rect(case_x * TILE_WIDTH + offset_x, case_y * TILE_HEIGHT + offset_y, TILE_WIDTH, TILE_HEIGHT)
            sprite_to_change.image = scene.tile_cache.get_image(tile['image'])

    def action_save_level(self, editor_scene):
        """
        Save the level on disk
        """
        #TODO
        pass
        # json_level = json.dumps(editor_scene.matrix_level)
        # with open('maps/level_1.json', 'w') as file:
        #     file.write(json_level)


class TerrainSprite(Sprite):
    """
    A Sprite representing the terrain
    Both image and rect are used to display the sprite
    """

    def __init__(self, rect, image):
        super(TerrainSprite, self).__init__()
        self.image = image
        self.rect = rect

    def update(self, camera):
        """
        We need to update the sprites if we move the camera
        :param camera: Camera
        """
        self.rect = self.rect.move(camera.last_move)
