from clash_of_clans_bot.nodes.sequence import Sequence
from clash_of_clans_bot.nodes.action import Action

def ShopBehavior(ctx):
    return (
        Sequence([
            Action(ctx.intention.is_set, "USE_BUILDER"),
            Action(ctx.intention.set, "BUILD_NEW"),
            Action(ctx.shop_controller.select_new_building),
        ])
    )