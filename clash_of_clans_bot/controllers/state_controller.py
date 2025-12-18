from clash_of_clans_bot.bot_logic.enums.state_enum import State
from clash_of_clans_bot.bot_logic.enums.status_enum import StatusEnum as Status
import os

class StateController:
    def __init__(self, vision):
        self._vision = vision
        self.state = State.UNKNOWN
        self.assets_path = os.path.join("clash_of_clans_bot", "bot_logic", "states")

    def _detect_state(self):
        for state in State:
            if state is State.UNKNOWN:
                continue

            identifier_dir = os.path.join(
                self.assets_path, state.value, "identifier_images"
            )

            for filename in os.listdir(identifier_dir):
                image_path = os.path.join(identifier_dir, filename)

                if self._vision.is_image_on_screen(image_path):
                    self.state = state
                    return

        self.state = State.UNKNOWN

    def is_on_state(self, state):
        if self.state == State.UNKNOWN:
            return Status.RUNNING
        return Status.SUCCESS if self.state == state else Status.FAILURE

    def on_tick(self):
        self._detect_state()
