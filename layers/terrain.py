from pygame.sprite import Group, Sprite


class TerrainGroup(Group):
    """
    A group of sprites representing the terrain
    At the base layer
    Every thing will drawn onto this
    """

    layer = 0

    def __init__(self, *sprites):
        super(TerrainGroup, self).__init__(*sprites)

    def update(self, camera):
        """call the update method of every member sprite
        Calls the update method of every member sprite. All arguments that
        were passed to this method are passed to the Sprite update function.
        """
        for s in self.sprites():
            s.update(camera)


class Terrain(Sprite):
    """
    A Sprite representing the terrain
    Both image and rect are used to display the sprite
    """

    def __init__(self, rect, image):
        super(Terrain, self).__init__()
        self.image = image
        self.rect = rect

    def update(self, camera):
        """
        We need to update the sprites if we move the camera
        :param camera: Camera
        """
        self.rect = self.rect.move(camera.last_move)
