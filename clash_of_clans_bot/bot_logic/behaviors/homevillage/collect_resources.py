from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)

CollectResourcesBehavior = (
    Parallel([
        Action(mouse.click_button, "images/home_village/gold_to_collect.png"),
        Action(mouse.click_button, "images/home_village/elixir_to_collect.png"),
    ],
        policy='Sequence'
    )
)