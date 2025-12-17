import pyautogui
import random
from clash_of_clans_bot.bot_logic.nodes.status import Status


class AttackController():
    def __init__(self, mouse, vision):
        self._mouse = mouse
        self._vision = vision

    def deploy_troops(self, count=5):
        for _ in range(count):
            x, y = self._vision.random_point()
            self._mouse.move(x, y, movement_duration=0.1)
            self._mouse.click()
        return Status.SUCCESS