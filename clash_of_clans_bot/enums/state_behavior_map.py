from clash_of_clans_bot.behaviors.disconnected_behavior import DisconnectedBehavior
from clash_of_clans_bot.behaviors.home_village_behavior import HomeVillageBehavior
from clash_of_clans_bot.behaviors.upgrade_menu_behavior import UpgradeMenuBehavior
from clash_of_clans_bot.behaviors.attack_menu_behavior import AttackMenuBehavior
from clash_of_clans_bot.behaviors.attack_behavior import AttackBehavior
from clash_of_clans_bot.behaviors.shop_behavior import ShopBehavior
from clash_of_clans_bot.behaviors.profile_behavior import ProfileBehavior
from clash_of_clans_bot.behaviors.homescreen_popup_behavior import HomeScreenPopupBehavior
from clash_of_clans_bot.enums.state_enum import State

STATE_BEHAVIOR_MAP = {
    State.HOME_VILLAGE: HomeVillageBehavior,
    State.UPGRADE_MENU: UpgradeMenuBehavior,
    State.ATTACK_MENU: AttackMenuBehavior,
    State.ATTACK: AttackBehavior,
    State.SHOP: ShopBehavior,
    State.PROFILE: ProfileBehavior,
    State.DISCONNECTED: DisconnectedBehavior,
    State.HOMESCREEN_POPUP: HomeScreenPopupBehavior,
}