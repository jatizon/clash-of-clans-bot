from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.nodes.selector import Selector
from clash_of_clans_bot.nodes.sequence import Sequence
from clash_of_clans_bot.nodes.always_success import AlwaysSuccess


def HomeVillageBehavior(ctx):
    return (
        Sequence([
            AlwaysSuccess(Sequence([
                Action(ctx.intention.not_set),
                Action(ctx.home_village_controller.unselect_building),
                Action(ctx.home_village_controller.center_screen),
                Action(ctx.home_village_controller.try_collect_resources),
            ])),
            Selector([
                Sequence([
                    Action(ctx.intention.is_set, "BUILD_NEW"),
                    Selector([
                        Sequence([
                            Action(ctx.home_village_controller.check_no_resources),
                            Action(ctx.home_village_controller.close_no_resources_popup)
                        ]),
                        Sequence([
                            Action(ctx.home_village_controller.try_build_new),
                            Action(ctx.intention.discard)
                        ])
                    ]),
                ]),
                Sequence([
                    Action(ctx.intention.is_set, "USE_BUILDER"),
                    Action(ctx.home_village_controller.choose_suggested_upgrade),
                    Action(ctx.intention.discard)
                ]),
                Sequence([
                    Action(ctx.home_village_controller.check_has_achievements),
                    Action(ctx.intention.set, "CLAIM_ACHIEVEMENT_REWARDS"),
                    Action(ctx.home_village_controller.open_profile)
                ]),
                Sequence([
                    Action(ctx.home_village_controller.has_low_resources),
                    Action(ctx.home_village_controller.start_attack)
                ]),
                Sequence([
                    Action(ctx.home_village_controller.check_has_builder),
                    Action(ctx.intention.set, "USE_BUILDER"),
                    Action(ctx.home_village_controller.open_suggested_upgrades)
                ]),
                Action(ctx.home_village_controller.start_attack),
            ])
        ])
    )