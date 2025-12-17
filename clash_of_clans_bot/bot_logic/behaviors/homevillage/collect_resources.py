from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence


def CollectResourcesBehavior(controller):
    return (
        Parallel([
            Action(controller.ui.click_button, "images/buttons/home_village/gold_to_collect.png"),
            Action(controller.ui.click_button, "images/buttons/home_village/elixir_to_collect.png"),
        ],
            policy='Sequence'
        )
    )