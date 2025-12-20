from enum import Enum

class State(Enum):
    UNKNOWN = "unknown"
    HOME_VILLAGE = "home_village"
    ATTACK = "attack"
    SHOP = "shop"
    DISCONNECTED = "disconnected"
