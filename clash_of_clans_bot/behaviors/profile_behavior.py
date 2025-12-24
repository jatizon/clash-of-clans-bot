from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.nodes.selector import Selector
from clash_of_clans_bot.nodes.sequence import Sequence


def ProfileBehavior(ctx):
    return (
        Selector([
            Sequence([
                Action(ctx.intention.is_set, "CLAIM_ACHIEVEMENT_REWARDS"),
                Action(ctx.profile_controller.claim_reward),
                Action(ctx.profile_controller.close_profile)
            ]),
        ])
    )