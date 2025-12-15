from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.always_success import AlwaysSuccess
from clash_of_clans_bot.bot_logic.nodes.inverter import Inverter
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.repeat import Repeat
from clash_of_clans_bot.bot_logic.nodes.selector import Selector
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.bot_logic.behaviors.utils.click_close_button import ClickCloseButtonUntilNotFoundBehavior
from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)

AttackBehavior = (
    Sequence([
        Action(mouse.click_button, "images/home_village/start_attack_1.png"),
        Action(mouse.click_button, "images/home_village/find_match.png"),
        Action(mouse.click_button, "images/home_village/start_attack_2.png"),
        Repeat(
            Action(mouse.click_button, "images/attacking/barbarian_attack_icon.png"),
            stop_on_success=True,
            times=20
        ),
        Repeat(
            Sequence([
                Action(mouse.deploy_troops),
                AlwaysSuccess(Action(mouse.click_button, "images/attacking/barbarian_attack_icon.png")),
                Selector([
                    Action(mouse.check_image_exists, "images/home_village/shop.png"),
                    Action(mouse.click_button, "images/attacking/return_home.png"),
                ]),
            ]),
            stop_on_success=True,
        ),
    ])
)