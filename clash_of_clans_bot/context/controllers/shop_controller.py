from clash_of_clans_bot.enums.status_enum import Status


class ShopController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision

    def select_new_building(self):
        arrow_position = self.vision.get_color_position((255, 186, 56))
        if not arrow_position:
            return Status.RUNNING
        arrow_position = (arrow_position[0]-100, arrow_position[1] + 100)
        self.mouse.move(arrow_position[0], arrow_position[1])
        self.mouse.click()
        return Status.RUNNING