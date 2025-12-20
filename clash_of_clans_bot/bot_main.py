import logging
from clash_of_clans_bot.behaviors.home_village_main import BotLogicBehaviorTree
from clash_of_clans_bot.drivers.mouse import Mouse
from clash_of_clans_bot.drivers.vision import Vision
from clash_of_clans_bot.context.context import Context
from pyclick import HumanClicker


logging.basicConfig(level=logging.INFO, format='%(message)s')

human_clicker = HumanClicker()
mouse = Mouse(human_clicker)
vision = Vision(images_path="clash_of_clans_bot")
context = Context(mouse, vision)

while True:
    context.state_controller.on_tick()
    BotLogicBehaviorTree(context).tick()