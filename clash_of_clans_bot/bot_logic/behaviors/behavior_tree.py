from clash_of_clans_bot.bot_logic.nodes.action import Action
from clash_of_clans_bot.bot_logic.nodes.sequence import Sequence
from clash_of_clans_bot.bot_logic.nodes.parallel import Parallel
from clash_of_clans_bot.bot_logic.nodes.repeat import Repeat
from clash_of_clans_bot.bot_logic.nodes.selector import Selector
from clash_of_clans_bot.bot_logic.behaviors.attack.attack_main import AttackBehavior
from clash_of_clans_bot.bot_logic.behaviors.homevillage.homevillage_main import HomeVillageBehavior
from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)

BotLogicBehaviorTree = Repeat(
    Selector([
        Action(mouse.click_button, "images/common/reopen_game.png"),
        Parallel([
            HomeVillageBehavior,
            AttackBehavior
        ],
        policy='Sequence')
    ]),
)