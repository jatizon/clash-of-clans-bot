from clash_of_clans_bot.context.controllers.attack_controller import AttackController
from clash_of_clans_bot.context.controllers.home_village_controller import HomeVillageController
from clash_of_clans_bot.context.controllers.state_controller import StateController
from clash_of_clans_bot.context.intention import Intention
from clash_of_clans_bot.context.controllers.profile_controller import ProfileController
from clash_of_clans_bot.context.controllers.upgrade_menu_controller import UpgradeMenuController
from clash_of_clans_bot.context.controllers.disconnected_controller import DisconnectedController
from clash_of_clans_bot.context.blackboard import Blackboard
from clash_of_clans_bot.context.controllers.shop_controller import ShopController
from clash_of_clans_bot.context.controllers.attack_menu_controller import AttackMenuController
from clash_of_clans_bot.context.controllers.homescreen_popup_controller import HomescreenPopupController


class Context():
    def __init__(self, mouse, vision):
        # Intention
        self.intention = Intention()

        # Blackboard
        self.blackboard = Blackboard()

        # Controllers
        self.attack_controller = AttackController(mouse, vision)
        self.attack_menu_controller = AttackMenuController(mouse, vision)
        self.home_village_controller = HomeVillageController(mouse, vision)
        self.state_controller = StateController(vision)
        self.profile_controller = ProfileController(mouse, vision)
        self.upgrade_menu_controller = UpgradeMenuController(mouse, vision)
        self.disconnected_controller = DisconnectedController(mouse, vision)
        self.shop_controller = ShopController(mouse, vision)
        self.homescreen_popup_controller = HomescreenPopupController(mouse, vision)