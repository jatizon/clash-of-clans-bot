import os

from clash_of_clans_bot.enums.status_enum import Status


class DisconnectedController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision
        self._images_base_path = "clash_of_clans_bot/images/disconnected/other"

    def connect(self):
        try:
            for image_file in os.listdir(self._images_base_path):
                if image_file.lower().endswith('.png'):
                    image_path = os.path.join(self._images_base_path, image_file)
                    normalized_path = image_path.replace(os.sep, '/')
                    position = self.vision.get_image_position(normalized_path)
                    if position:
                        self.mouse.move(position[0], position[1])
                        self.mouse.click()
                        return Status.SUCCESS
        except FileNotFoundError:
            pass
        return Status.FAILURE