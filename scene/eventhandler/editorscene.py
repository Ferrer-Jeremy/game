import json

import pygame

from utils import event


class EditorSceneEventHandler:

    def __init__(self):
        self.selected_case = 0

    def __call__(self, editor_scene, events):
        if events.get(event.M_LEFT, 0) == 1:
            self.action_replace_case(editor_scene)

        if events.get(pygame.K_e, 0) == 1:
            self.action_save_level(editor_scene)

        if events.get(pygame.K_a, 0) == 1:
            editor_scene.reset_with_size()

        if events.get(pygame.K_r, 0) == 1:
            self.change_selected_case()

    def action_replace_case(self, editor_scene):
        """
        Replace at the cursor pos the case by the case_selected
        Then reload the terrain
        """
        cursor_x, cursor_y = pygame.mouse.get_pos()
        cursor_x = cursor_x - editor_scene.offset_x
        cursor_y = cursor_y - editor_scene.offset_y
        case_x = cursor_x // editor_scene.tile_width
        case_y = cursor_y // editor_scene.tile_height
        limit_x = editor_scene.case_length_width
        limit_y = editor_scene.case_length_height

        # We check if the cursor is in the map
        if 0 <= case_x < limit_x and 0 <= case_y < limit_y:
            editor_scene.matrix_level[case_y][case_x] = self.selected_case
            editor_scene.terrain_group = editor_scene.load_terrain_group()

    def action_save_level(self, editor_scene):
        """
        Save the level on disk
        """
        json_level = json.dumps(editor_scene.matrix_level)
        with open('maps/level_1.json', 'w') as file:
            file.write(json_level)

    def change_selected_case(self):
        self.selected_case += 1
        if self.selected_case > 3:
            self.selected_case = 0
