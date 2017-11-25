import json

import pygame

from utils import event


class PlaySceneEventHandler:

    def __init__(self):
        self.selected_case = 0

    def __call__(self, editor_scene, events):
        pass
        # if events.get(event.M_LEFT, 0) == 1:
            # self.action_replace_case(editor_scene)


