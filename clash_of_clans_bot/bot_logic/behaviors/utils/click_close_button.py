from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.repeat import Repeat
from clash_of_clans_bot.bot_logic.nodes.selector import Selector
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)

ClickCloseButtonUntilNotFoundBehavior = (
    Repeat(
        Selector([
            # Try all close button images, some work in many cases
            Action(mouse.click_button, "images/common/close_1_shop.png"),
            Action(mouse.click_button, "images/common/close_2_profile.png"),
            Action(mouse.click_button, "images/common/shield_close.png")
        ]),
        stop_on_failure=True
    )
)