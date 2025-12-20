from clash_of_clans_bot.context import intentions
from clash_of_clans_bot.context.controllers import home_village_controller
from clash_of_clans_bot.nodes.Sequence import Sequence
from clash_of_clans_bot.nodes.always_success import AlwaysSuccess

def HomeVillageBehavior(ctx):
    return (
        Sequence([
            Action(ctx.home_village_controller.try_collect_resources),
            Selector([
                Sequence([
                    Action(ctx.home_village_controller.has_achievements),
                    AlwaysSuccess(Action(ctx.intentions.set("CLAIM_ACHIEVEMENT_REWARDS"))),
                    Action(ctx.home_village_controller.open_profile)
                ]),
                Sequence([
                    Action(ctx.home_village_controller.has_builder),
                    Action(ctx.home_village_controller.try_make_upgrade),
                ]),
            ]),
                Action(ctx.home_village_controller.try_collect_resources),
            ])
            Action(ctx.home_village_controller.try_collect_resources),
        ])
    )