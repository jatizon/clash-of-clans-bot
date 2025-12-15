from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.inverter import Inverter
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.bot_logic.behaviors.utils.click_close_button import ClickCloseButtonUntilNotFoundBehavior
from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)

NewAchievementsBehavior = (
    Parallel([
        Sequence([
            Action(mouse.click_button, "images/home_village/new_achievement.png"),
            Action(mouse.click_button, "images/home_village/claim_achievement.png"),
        ]),
        Inverter(ClickCloseButtonUntilNotFoundBehavior)
    ],
        policy='Sequence'
    )
)