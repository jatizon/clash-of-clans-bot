from clash_of_clans_bot.nodes.action import Action
from clash_of_clans_bot.nodes.sequence import Sequence


def HomeScreenPopupBehavior(ctx):
    return (
        Sequence([
            Action(ctx.homescreen_popup_controller.close_popup),
        ])
    )

