import logging
from clash_of_clans_bot.bot_logic.behaviors.behavior_tree import BotLogicBehaviorTree
from clash_of_clans_bot.drivers.mouse import Mouse
from clash_of_clans_bot.drivers.vision import Vision
from clash_of_clans_bot.controllers.main_controller import MainController
from pyclick import HumanClicker


logging.basicConfig(level=logging.INFO, format='%(message)s')

human_clicker = HumanClicker()
mouse = Mouse(human_clicker)
vision = Vision(images_path="clash_of_clans_bot")
controller = MainController(mouse, vision)

while True:
    controller.state_controller.on_tick()
    BotLogicBehaviorTree(controller).tick()