from scene.editorscene import EditorScene


class SceneManager:
    """
    Save, Load, Change between scene
    """

    def __init__(self):
        self.current_scene = None
        self.current_type_scene = None

    def load_scene(self, scene_name, scene_type='editor_scene'):
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

