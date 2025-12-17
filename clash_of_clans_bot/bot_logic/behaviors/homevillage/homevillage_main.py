from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence

from clash_of_clans_bot.bot_logic.behaviors.homevillage.collect_resources import CollectResourcesBehavior
from clash_of_clans_bot.bot_logic.behaviors.homevillage.new_achievement import NewAchievementsBehavior
from clash_of_clans_bot.bot_logic.behaviors.homevillage.use_builder import UseBuilderBehavior


def HomeVillageBehavior(controller):
    return (
        Parallel([
            Action(controller.ui.adjust_screen),
            NewAchievementsBehavior(controller),
            CollectResourcesBehavior(controller),
            UseBuilderBehavior(controller)
        ],
            policy='Sequence')
    )