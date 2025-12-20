import time
from clash_of_clans_bot.controllers.attack_controller import AttackController
from clash_of_clans_bot.controllers.ui_controller import UIController
from clash_of_clans_bot.controllers.state_controller import StateController
from clash_of_clans_bot.context.intentions import Intentions

class Context():
    def __init__(self, mouse, vision):
        # Intention
        self.intentions = Intentions()

        # Controllers
        self.attack_controller = AttackController(mouse, vision)
        self.home_village_controller = HomeVillageController(mouse, vision)
        self.ui_controller = UIController(mouse, vision)
        self.state_controller = StateController(vision)