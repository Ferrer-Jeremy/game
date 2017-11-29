import json
from utils.settings import *
from scene.playscene import PlayScene
from scene.editorscene import EditorScene


class SceneManager:

    def __init__(self):
        self.current_scene = None
        self.current_type_scene = None

    def load_scene(self, scene_type, scene_name, start_scene_mode=None):
        """
        Load a scene from disk
        :param scene_type: str
        :param scene_name: str
        :param start_scene_mode: str
        :return: Scene subclass -> EditorScene or ...
        """
        self.current_scene = scene_name
        self.current_type_scene = scene_type
        if scene_type == 'editor_scene':
            matrix_level = self.from_scene_name(scene_name)
            return EditorScene(matrix_level, start_scene_mode=start_scene_mode)

        if scene_type == 'play_scene':
            matrix_level = self.from_scene_name(scene_name)
            return PlayScene(matrix_level, start_scene_mode=start_scene_mode)

        raise NotImplementedError('scene not found')

    def from_matrix_level(self, matrix_level):
        """
        Instanciate the raw_level
        The sub list must all have the same size
        :param matrix_level: [[int, int, ...], [int, int, ...], ...]
        :return: Level
        """
        if not isinstance(matrix_level, list):
            raise TypeError('raw_level is not a list')
        if len(matrix_level) == 0:
            raise ValueError('raw_level is empty')
        if not isinstance(matrix_level[0], list):
            raise TypeError('raw_level elements are not list')

        width = len(matrix_level[0])
        for line in matrix_level:
            if width != len(line):
                raise ValueError('raw_level has not the same size on each line')

        return matrix_level

    def from_scene_name(self, scene_name):
        """
        Instanciate the scene from a json file
        :param scene_name: str
        :return: EditorScene
        """
        filename = '{}/{}.json'.format(FOLDER_EDITOR_SCENE, scene_name)
        with open(filename, 'r', encoding='utf8') as file:
            content = file.read()
            raw_level = json.loads(content)

        return self.from_matrix_level(raw_level)
