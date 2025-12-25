from clash_of_clans_bot.enums.status_enum import Status
import os


class HomescreenPopupController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision

    def close_popup(self):
        for image in os.listdir("clash_of_clans_bot/images/homescreen_popup/other"):
            image_path = os.path.join("clash_of_clans_bot/images/homescreen_popup/other", image)
            close_popup_position = self.vision.get_image_position(image_path)
            if close_popup_position:
                self.mouse.move(close_popup_position[0], close_popup_position[1])
                self.mouse.click()
                return Status.SUCCESS
        return Status.SUCCESS
