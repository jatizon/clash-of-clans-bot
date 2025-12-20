
from clash_of_clans_bot.enums.status_enum import StatusEnum as Status


class UIController:
    def __init__(self, mouse, vision):
        self._mouse = mouse
        self._vision = vision

    def click_button(self, image_path, delta_x=0, delta_y=0):
        position = self._vision.get_image_position(image_path)
        if not position:
            return Status.FAILURE
        self._mouse.move(position[0]+delta_x, position[1]+delta_y)
        self._mouse.click()
        return Status.SUCCESS

    def adjust_screen(self):
        return self._mouse.adjust_screen()

    def detect(self, image_path):
        is_on_screen = self._vision.is_image_on_screen(image_path)
        return Status.SUCCESS if is_on_screen else Status.FAILURE

    