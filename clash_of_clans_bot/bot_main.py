import logging
from clash_of_clans_bot.bot_logic.behaviors.behavior_tree import BotLogicBehaviorTree

logging.basicConfig(level=logging.INFO, format='%(message)s')

BotLogicBehaviorTree.run()