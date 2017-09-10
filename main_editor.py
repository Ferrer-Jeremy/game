import sys

import pygame
from utils.settings import *
from scene import SceneManager
from utils import event


def exit_program(event_dict):
    if event_dict.get(pygame.QUIT, False):
        sys.exit()

pygame.init()

screen_size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(screen_size)


scene_manager = SceneManager()
editor_scene = scene_manager.load_scene('level_2', 'editor_scene')


clock = pygame.time.Clock()
events = {}

while 1:
    clock.tick(60)

    events = event.get_events(events)
    exit_program(events)
    editor_scene.check_events(events)

    screen.fill((0, 0, 0))
    editor_scene.update_and_draw(screen)
    pygame.display.update()
