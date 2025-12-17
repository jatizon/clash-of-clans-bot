from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.inverter import Inverter
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.repeat import Repeat
from clash_of_clans_bot.bot_logic.nodes.selector import Selector
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.bot_logic.behaviors.util_behaviors.click_close_button import ClickCloseButtonUntilNotFoundBehavior


def _NewBuildingBehavior(controller):
    return (
        Selector([
            Sequence([
                Action(controller.ui.click_button, "images/buttons/home_village/build_new.png", delta_y=-100),
                Action(controller.ui.click_button, "images/buttons/home_village/confirm_new_building.png"),
            ]),
            Sequence([
                Action(controller.ui.click_button, "images/buttons/home_village/build_new.png", delta_y=-500),
                Action(controller.ui.click_button, "images/buttons/home_village/confirm_new_building.png"),
            ])
        ])
    )


def _UpgradeBuildingBehavior(controller):
    return (
        Sequence([
            Action(controller.ui.click_button, "images/buttons/home_village/upgrade.png"),
            Action(controller.ui.click_button, "images/buttons/home_village/confirm_upgrade.png"),
            Selector([
                Inverter(
                    Action(controller.ui.detect, "images/identifiers/home_village/insuficient_gold.png")
                ),
                Inverter(
                    Action(controller.ui.detect, "images/identifiers/home_village/insuficient_elixir.png")
                ),
            ])
        ])
    )


def UseBuilderBehavior(controller):
    return (
        Repeat(
            Selector([
                Parallel([
                    Sequence([
                        Action(controller.ui.click_button, "images/buttons/home_village/builder_suggestions.png"),
                        Action(controller.ui.click_button, "images/buttons/home_village/suggested_upgrades.png", delta_y=35),
                        Selector([
                            _NewBuildingBehavior(controller),
                            _UpgradeBuildingBehavior(controller)
                        ]),
                    ]),
                    Inverter(ClickCloseButtonUntilNotFoundBehavior(controller))
                ],
                    policy='Sequence'
                ),
                Parallel([
                    Sequence([
                        Action(controller.ui.click_button, "images/buttons/home_village/builder_suggestions.png"),
                        Action(controller.ui.click_button, "images/buttons/home_village/suggested_upgrades.png", delta_y=100),
                        Selector([
                            _NewBuildingBehavior(controller),
                            _UpgradeBuildingBehavior(controller)
                        ])
                    ]),
                    Inverter(ClickCloseButtonUntilNotFoundBehavior(controller))
                ],
                    policy='Sequence'
                )
            ]),
            times=5,
            stop_on_failure=True
        )
    )