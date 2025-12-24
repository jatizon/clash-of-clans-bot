

from clash_of_clans_bot.nodes.sequence import Sequence
from clash_of_clans_bot.nodes.always_success import AlwaysSuccess
from clash_of_clans_bot.nodes.action import Action


def AttackMenuBehavior(ctx):
    return (
        Sequence([
            AlwaysSuccess(Sequence([
                Action(ctx.attack_menu_controller.is_army_camp_not_full),
                Action(ctx.intention.set, "FILL_ARMY_CAMP"),
                Action(ctx.attack_menu_controller.fill_army_camp)
            ])),
            Action(ctx.attack_menu_controller.find_village_to_attack)
        ])
    )