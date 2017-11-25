from scene.editorscene import EditorScene
from scene.playscene import PlayScene


class SceneManager:
    """
    Save, Load, Change between scene
    """

    def __init__(self):
        self.current_scene = None
        self.current_type_scene = None

    def load_scene(self, scene_name, scene_type):
        """
        Load a scene from disk
        :param scene_name: str
        :param scene_type: str
        :return: Scene subclass -> EditorScene or ...
        """
        self.current_scene = scene_name
        self.current_type_scene = scene_type
        if scene_type == 'editor_scene':
            return EditorScene.from_scene_name(scene_name)

        if scene_type == 'play_scene':
            return PlayScene.from_scene_name(scene_name)

