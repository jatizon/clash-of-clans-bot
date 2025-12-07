import logging
from btree import Status, Sequence, Selector, Action, Repeat
from mouse import Mouse

logging.basicConfig(level=logging.INFO, format='%(message)s')

mouse = Mouse()


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