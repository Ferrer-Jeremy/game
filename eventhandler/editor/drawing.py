import pygame

from utils import event


class DrawingEventHandler:

    def __call__(self, scene, events):
        if events.get(event.M_LEFT, 0) == 1:
            scene.terrain_group.action_replace_case(scene)

        if events.get(pygame.K_e, 0) == 1:
            scene.terrain_group.action_save_level(scene)

        if events.get(pygame.K_a, 0) == 1:
            scene.reset_with_size()

        if events.get(pygame.K_r, 0) == 1:
            scene.drawing_scene_mode.action_change_selected_case()




