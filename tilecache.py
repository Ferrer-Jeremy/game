import pygame


class TileCache:
    """Load the tilesets lazily into global cache"""

    image_folder = 'images'

    def __init__(self):
        self.cache = {}

    def get_image(self, name):
        """
        Return a tile, load it from disk if needed.
        :param name: string
        :return Surface
        """

        key = name
        return self.cache.get(key, self._load_tile(name))

    def _load_tile(self, name):
        """
        Load an image by it's name
        :param name: string
        :return Surface
        """

        image = pygame.image.load('{}/{}'.format(self.image_folder, name))
        return image.convert()
