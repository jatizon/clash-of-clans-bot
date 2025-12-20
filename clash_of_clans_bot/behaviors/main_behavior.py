from clash_of_clans_bot.nodes.selector import Selector
from clash_of_clans_bot.nodes.sequence import Sequence
from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.enums.state_enum import State
from clash_of_clans_bot.nodes.always_success import AlwaysSuccess

def BotLogicBehaviorTree(ctx):
    return (
        Selector([
            Sequence([
                Action(ctx.state_controller.is_on_state, State.DISCONNECTED),
                AlwaysSuccess(DisconnectedBehavior(ctx)),
            ]),
            Sequence([
                Action(ctx.state_controller.is_on_state, State.HOME_VILLAGE),
                AlwaysSuccess(HomeVillageBehavior(ctx)),
            ]),
            Sequence([
                Action(ctx.state_controller.is_on_state, State.ATTACK),
                AlwaysSuccess(AttackBehavior(ctx)),
            ]),
            UnknownBehavior(ctx),
        ])
    )
