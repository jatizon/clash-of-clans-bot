import os
from re import S

from clash_of_clans_bot.enums.state_enum import State
from clash_of_clans_bot.enums.status_enum import Status

class StateController:
    def __init__(self, vision):
        self._vision = vision
        self.state = State.UNKNOWN
        self._images_base_path = "clash_of_clans_bot/images"
        self.state_check_order = [
            State.DISCONNECTED,
            State.HOMESCREEN_POPUP,
            State.UPGRADE_MENU,
            State.PROFILE,
            State.ATTACK_MENU,
            State.HOME_VILLAGE,
            State.ATTACK,
            State.SHOP
        ]

    def _detect_state(self):
        for state in self.state_check_order:
            state_name = state.value
            
            identifiers_path = os.path.join(self._images_base_path, state_name, "identifiers")
            
            try:
                for image_file in os.listdir(identifiers_path):
                    if image_file.lower().endswith('.png'):
                        image_path = os.path.join(identifiers_path, image_file)
                        normalized_path = image_path.replace(os.sep, '/')
                        if self._vision.is_image_on_screen(normalized_path):
                            return state
            except FileNotFoundError:
                continue
        return State.UNKNOWN

    def is_on_state(self, state):
        if self.state == State.UNKNOWN:
            return Status.RUNNING
        return Status.SUCCESS if self.state == state else Status.FAILURE

    def is_on_state_now(self, state):
        current_state = self._detect_state()
        return current_state == state

    def on_tick(self):
        print("State: ", self.state)
        self.state = self._detect_state()
