import sys
import pygame
from level import Level
from camera import Camera
import event


def exit_program(event_dict):
    if event_dict.get(pygame.QUIT, False):
        sys.exit()

pygame.init()

screen_size = screen_width, screen_height = 660, 400
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

level = Level.from_json_file('maps/level_1.json')
terrain = level.terrain_group

camera = Camera(screen_width, screen_height, level.width, level.height)

events = {}

while 1:
    clock.tick(60)

    events = event.get_events(events)
    exit_program(events)
    camera.check_events(events)

    if events.get(pygame.K_e, 0) == 1:
        level.save_level()

    if events.get(event.M_LEFT, 0) == 1:
        pos = pygame.mouse.get_pos()
        # print(events[event.M_LEFT])
        # print(pos)
        level.add_case(pos)

    screen.fill((0, 0, 0))
    level.terrain_group.update(camera)
    level.terrain_group.draw(screen)
    pygame.display.update()
