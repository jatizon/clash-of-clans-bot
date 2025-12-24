from clash_of_clans_bot.enums.status_enum import Status

class UpgradeMenuController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision

    def try_upgrade(self):
        upgrade_position = self.vision.get_image_position("clash_of_clans_bot/images/upgrade_menu/other/confirm.png")
        if upgrade_position:
            self.mouse.move(upgrade_position[0], upgrade_position[1])
            self.mouse.click()
            return Status.SUCCESS
        build_clan_castle_position = self.vision.get_image_position("clash_of_clans_bot/images/upgrade_menu/other/build_clan_castle.png")
        if build_clan_castle_position:
            self.mouse.move(build_clan_castle_position[0], build_clan_castle_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def check_no_resources(self):
        is_on_screen = self.vision.is_image_on_screen("clash_of_clans_bot/images/upgrade_menu/other/no_resources.png")
        return Status.SUCCESS if is_on_screen else Status.FAILURE

    def close_upgrade_menu(self):
        close_position1 = self.vision.get_image_position("clash_of_clans_bot/images/upgrade_menu/other/close1.png")
        close_position2 = self.vision.get_image_position("clash_of_clans_bot/images/upgrade_menu/other/close2.png")
        if close_position1:
            self.mouse.move(close_position1[0], close_position1[1])
            self.mouse.click()
            return Status.RUNNING
        if close_position2:
            self.mouse.move(close_position2[0], close_position2[1])
            self.mouse.click()
        return Status.SUCCESS

