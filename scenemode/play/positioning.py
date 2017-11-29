from layers.positioning import PositionningGroup


class PositioningMode:

    def __init__(self):
        self.positioning_sprites = PositionningGroup.load()

    def update(self, camera):
        self.positioning_sprites.update(camera)

    def draw(self, screen):
        self.positioning_sprites.draw(screen)
