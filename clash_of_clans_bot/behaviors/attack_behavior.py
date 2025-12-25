from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.nodes.sequence import Sequence
from clash_of_clans_bot.nodes.selector import Selector



def AttackBehavior(ctx):
    return (
        Selector([
            Sequence([
                Action(ctx.attack_controller.did_attack_end),
                Action(ctx.attack_controller.go_back_to_home_village)
            ]),
            Sequence([
                Action(ctx.attack_controller.select_troop),
                Action(ctx.attack_controller.deploy_troops)
            ]),
        ])
    )