from clash_of_clans_bot.enums.state_enum import State
from clash_of_clans_bot.enums.image_enum import StatesImages
from clash_of_clans_bot.enums.status_enum import StatusEnum as Status
import os

class StateController:
    def __init__(self, vision):
        self._vision = vision
        self.state = State.UNKNOWN

    def _detect_state(self):
        for state in vars(StatesImages).values():
            for identifier in state.IDENTIFIER_IMAGES:
                if self._vision.is_image_on_screen(identifier.value):
                    self.state = state
                    return

        self.state = State.UNKNOWN

    def is_on_state(self, state):
        if self.state == State.UNKNOWN:
            return Status.RUNNING
        return Status.SUCCESS if self.state == state else Status.FAILURE

    def on_tick(self):
        print("State: ", self.state)
        self._detect_state()
