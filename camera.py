import pygame
from pygame import Rect


class Camera:

    def __init__(self, camera_width, camera_height, level_width, level_height):
        self.last_move = None
        self.rect = Rect(0, 0, camera_width, camera_height)
        self.level_size = self.level_width, self.level_height = level_width, level_height

    def move_of(self, x, y):
        """
        From the actual position x and y represent the movement done to get to the final position
        :param x: int (18, -12, ...)
        :param y: int (3, -56, ...)
        """
        self.last_move = (x, y)
        self.rect = self.rect.move(x, y)

    def check_events(self, event_dict):
        xx = yy = 10
        x = y = 0

        if event_dict.get(pygame.K_UP, 0) > 0:
            y = y + yy

        if event_dict.get(pygame.K_DOWN, 0) > 0:
            y = y - yy

        if event_dict.get(pygame.K_LEFT, 0) > 0:
            x = x + xx

        if event_dict.get(pygame.K_RIGHT, 0) > 0:
            x = x - xx

        self.move_of(x, y)
