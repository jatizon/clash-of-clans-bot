from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.nodes.sequence import Sequence


def DisconnectedBehavior(ctx):
    return (
        Sequence([
            Action(ctx.intention.discard),
            Action(ctx.disconnected_controller.connect)
        ])
    )