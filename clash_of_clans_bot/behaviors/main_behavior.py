from clash_of_clans_bot.enums.state_enum import State
from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.nodes.always_success import AlwaysSuccess
from clash_of_clans_bot.nodes.selector import Selector
from clash_of_clans_bot.nodes.sequence import Sequence
from clash_of_clans_bot.enums.state_behavior_map import STATE_BEHAVIOR_MAP


def BotLogicBehaviorTree(ctx):
    return (
        Selector([
                Sequence([
                    Action(ctx.state_controller.is_on_state, state),
                    AlwaysSuccess(STATE_BEHAVIOR_MAP[state](ctx)),
                ]) for state in State if state != State.UNKNOWN
        ])
    )
