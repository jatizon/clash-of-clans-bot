import logging
from clash_of_clans_bot.bot_logic.nodes.status import Status
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence
from clash_of_clans_bot.bot_logic.nodes.selector import Selector
from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.repeat import Repeat
from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

logging.basicConfig(level=logging.INFO, format='%(message)s')

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)


btree = Sequence([
    Action(mouse.click_button, "buttons/home_village/start_attack_1.png"),
    Action(mouse.click_button, "buttons/home_village/find_match.png"),
    Action(mouse.click_button, "buttons/home_village/start_attack_2.png"),
    Repeat(
        Action(mouse.click_button, "buttons/attacking/barbarian_attack_icon.png"),
        stop_on_success=True,
        times=20
    ),
    Repeat(
        Sequence([
            Action(mouse.deploy_troops),
            Selector([
                Action(mouse.check_image_exists, "buttons/home_village/shop.png"),
                Action(mouse.click_button, "buttons/attacking/return_home.png"),
            ])
        ]),
        stop_on_success=True,
        times=20
    )
])

btree.run()