import inspect
from abc import ABCMeta, abstractmethod


class Scene(metaclass=ABCMeta):

    @abstractmethod
    def check_events(self, events):
        """
        Check the events to execute actions
        :param events: dict events containing their duration
        """
        NotImplementedError("Class {} doesn't implement {}".format(self.__class__.__name__, inspect.currentframe()))

    def update_and_draw(self, screen):
        """
        Update & draw on the screen all Sprites
        :param screen: Screen
        """
        NotImplementedError("Class {} doesn't implement {}".format(self.__class__.__name__, inspect.currentframe()))



