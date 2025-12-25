from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.nodes.selector import Selector
from clash_of_clans_bot.nodes.sequence import Sequence


def UpgradeMenuBehavior(ctx):
    return (
        Selector([
            Sequence([
                Action(ctx.upgrade_menu_controller.check_no_resources),
                Action(ctx.upgrade_menu_controller.close_upgrade_menu),
            ]),
            Action(ctx.upgrade_menu_controller.try_upgrade),
        ])
    )