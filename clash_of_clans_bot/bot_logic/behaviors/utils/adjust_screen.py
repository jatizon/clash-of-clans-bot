from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)

AdjustScreenBehavior = (
    Sequence([
        Action(mouse.zoom_out),
        Action(mouse.center_screen_clash)
    ])
)