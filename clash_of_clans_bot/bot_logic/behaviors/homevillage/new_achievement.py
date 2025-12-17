from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.inverter import Inverter
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.bot_logic.behaviors.util_behaviors.click_close_button import ClickCloseButtonUntilNotFoundBehavior


def NewAchievementsBehavior(controller):
    return (
        Parallel([
            Sequence([
                Action(controller.ui.click_button, "images/buttons/home_village/new_achievement.png"),
                Action(controller.ui.click_button, "images/buttons/home_village/claim_achievement.png"),
            ]),
            Inverter(ClickCloseButtonUntilNotFoundBehavior(controller))
        ],
            policy='Sequence'
        )
    )