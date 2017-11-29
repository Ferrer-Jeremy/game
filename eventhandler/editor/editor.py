

class EditorSceneEventHandler:

    def __init__(self, scene_mode_event_handler):
        self.scene_mode_event_handler = scene_mode_event_handler

    def __call__(self, scene, events):
        if self.scene_mode_event_handler:
            self.scene_mode_event_handler(scene, events)
