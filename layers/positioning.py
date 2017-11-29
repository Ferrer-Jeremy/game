from pygame.sprite import Group, Sprite
from pygame import Surface
from pygame import Rect
from pygame.color import Color
from utils.settings import *


class PositionningGroup(Group):
    """
    A group of sprites representing the terrain
    At the base layer
    Every thing will drawn onto this
    """

    layer = 0

    def __init__(self, *sprites):
        super(PositionningGroup, self).__init__(*sprites)

    @classmethod
    def load(cls):
        """
        Load all the json file tiles as Terrain(Sprite)
        And return them as a SpriteGroup -> TerrainGroup
        :return TerrainGroup
        """
        list_tiles = []
        offset_x = 0
        offset_y = 0
        image = Surface([TILE_WIDTH - 5, TILE_HEIGHT - 5])
        image.fill(Color(255, 255, 255, 255))

        for y in range(5):
            for x in range(5):
                rect = Rect(x * TILE_WIDTH + offset_x, y * TILE_HEIGHT + offset_y, TILE_WIDTH - 5, TILE_HEIGHT - 5)
                sprite = PositionningSprite(rect, image)
                list_tiles.append(sprite)

        return cls(list_tiles)

    def update(self, camera):
        """call the update method of every member sprite
        Calls the update method of every member sprite. All arguments that
        were passed to this method are passed to the Sprite update function.
        """
        for s in self.sprites():
            s.update(camera)


class PositionningSprite(Sprite):
    """
    A Sprite representing the terrain
    Both image and rect are used to display the sprite
    """

    def __init__(self, rect, image):
        super(PositionningSprite, self).__init__()
        self.image = image
        self.rect = rect

    def update(self, camera):
        """
        We need to update the sprites if we move the camera
        :param camera: Camera
        """
        self.rect = self.rect.move(camera.last_move)
