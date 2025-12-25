from enum import Enum

class State(Enum):
    UNKNOWN = "unknown"
    HOME_VILLAGE = "home_village"
    ATTACK = "attack"
    SHOP = "shop"
    DISCONNECTED = "disconnected"
    PROFILE = "profile"
    UPGRADE_MENU = "upgrade_menu"
    ATTACK_MENU = "attack_menu"
    HOMESCREEN_POPUP = "homescreen_popup"