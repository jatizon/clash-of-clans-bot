from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.always_success import AlwaysSuccess
from clash_of_clans_bot.bot_logic.nodes.inverter import Inverter
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.repeat import Repeat
from clash_of_clans_bot.bot_logic.nodes.selector import Selector
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.bot_logic.behaviors.util_behaviors.click_close_button import ClickCloseButtonUntilNotFoundBehavior


def AttackBehavior(controller):
    return (
        Sequence([
            Action(controller.ui.click_button, "images/buttons/home_village/start_attack_1.png"),
            Action(controller.ui.click_button, "images/buttons/home_village/find_match.png"),
            Action(controller.ui.click_button, "images/buttons/home_village/start_attack_2.png"),
            Repeat(
                Action(controller.ui.click_button, "images/buttons/attacking/barbarian_attack_icon.png"),
                stop_on_success=True,
                times=20
            ),
            Repeat(
                Sequence([
                    Action(controller.attack.deploy_troops),
                    AlwaysSuccess(Action(controller.ui.click_button, "images/buttons/attacking/barbarian_attack_icon.png")),
                    Selector([
                        Action(controller.ui.detect, "images/buttons/home_village/shop.png"),
                        Action(controller.ui.click_button, "images/buttons/attacking/return_home.png"),
                    ]),
                ]),
                stop_on_success=True,
            ),
        ])
    )