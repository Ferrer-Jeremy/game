from utils import Camera

from utils import TileCache
from scene import Scene
from layers import TerrainGroup
from eventhandler.play import PlaySceneEventHandler, PositioningEventHandler
from utils.settings import *
from scenemode.play import PositioningMode


class PlayScene(Scene):

    def __init__(self, level_matrix, start_scene_mode=None):
        """
        Instanciate the raw_level
        :param level_matrix: [[int, int, ...], [int, int, ...], ...]
        :param start_scene_mode: str
        :return PlayScene
        """
        self.level_matrix = level_matrix
        self.tile_cache = TileCache()
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.terrain_group = TerrainGroup.load(self.level_matrix, self.tile_cache)

        self.positioning_event_handler = PositioningEventHandler()
        self.positioning_scene_mode = PositioningMode()

        if start_scene_mode:
            # TODO get name then class
            self.event_handler_enabled = ''
            self.scene_mode_enabled = ''
        else:
            self.scene_event_handler = PlaySceneEventHandler(self.positioning_event_handler)
            self.scene_mode_enabled = self.positioning_scene_mode

    def check_events(self, events):
        """
        Check the events to execute actions
        :param events: dict events containing their duration
        """
        self.camera.check_events(events)
        self.scene_event_handler(self, events)

    def update_and_draw(self, screen):
        """
        Update & draw on the screen all Sprites
        :param screen: Screen
        """
        self.terrain_group.update(self.camera)
        self.scene_mode_enabled.update(self.camera)
        self.terrain_group.draw(screen)
        self.scene_mode_enabled.draw(screen)
