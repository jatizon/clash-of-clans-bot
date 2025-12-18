import time
from clash_of_clans_bot.controllers.attack_controller import AttackController
from clash_of_clans_bot.controllers.ui_controller import UIController
from clash_of_clans_bot.controllers.state_controller import StateController


class MainController():
    def __init__(self, mouse, vision):
        self.attack = AttackController(mouse, vision)
        self.ui = UIController(mouse, vision)
        self.state_controller = StateController(vision)