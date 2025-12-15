from clash_of_clans_bot.bot_logic.nodes.action import Action
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

_NewBuildingBehavior = (
    Selector([
        Sequence([
            Action(mouse.click_button, "images/home_village/build_new.png", delta_y=-100),
            Action(mouse.click_button, "images/home_village/confirm_new_building.png"),
        ]),
        Sequence([
            Action(mouse.click_button, "images/home_village/build_new.png", delta_y=-500),
            Action(mouse.click_button, "images/home_village/confirm_new_building.png"),
        ])
    ])
)

_UpgradeBuildingBehavior = (
    Sequence([
        Action(mouse.click_button, "images/home_village/upgrade.png"),
        Action(mouse.click_button, "images/home_village/confirm_upgrade.png"),
        Selector([
            Inverter(
                Action(mouse.check_image_exists, "images/home_village/insuficient_gold.png")
            ),
            Inverter(
                Action(mouse.check_image_exists, "images/home_village/insuficient_elixir.png")
            ),
        ])
    ])
)

UseBuilderBehavior = (
    Repeat(
        Selector([
            Parallel([
                Sequence([
                    Action(mouse.click_button, "images/home_village/builder_suggestions.png"),
                    Action(mouse.click_button, "images/home_village/suggested_upgrades.png", delta_y=35),
                    Selector([
                        _NewBuildingBehavior,
                        _UpgradeBuildingBehavior
                    ]),
                ]),
                Inverter(ClickCloseButtonUntilNotFoundBehavior)
            ],
                policy='Sequence'
            ),
            Parallel([
                Sequence([
                    Action(mouse.click_button, "images/home_village/builder_suggestions.png"),
                    Action(mouse.click_button, "images/home_village/suggested_upgrades.png", delta_y=100),
                    Selector([
                        _NewBuildingBehavior,
                        _UpgradeBuildingBehavior
                    ])
                ]),
                Inverter(ClickCloseButtonUntilNotFoundBehavior)
            ],
                policy='Sequence'
            )
        ]),
        times=5,
        stop_on_failure=True
    )
)