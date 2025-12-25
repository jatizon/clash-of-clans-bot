from clash_of_clans_bot.enums.status_enum import Status


class AttackMenuController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision

    def is_army_camp_not_full(self):
        army_camp_not_full_position = self.vision.get_image_position("clash_of_clans_bot/images/attack_menu/other/army_camp_not_full.png")
        if army_camp_not_full_position:
            return Status.SUCCESS
        return Status.FAILURE

    def fill_army_camp(self):
        army_camp_not_full_position = self.vision.get_image_position("clash_of_clans_bot/images/attack_menu/other/army_camp_not_full.png")
        if army_camp_not_full_position:
            self.mouse.move(army_camp_not_full_position[0], army_camp_not_full_position[1]+50)
            self.mouse.safe_click()
        barbarian_icon_position = self.vision.get_image_position("clash_of_clans_bot/images/attack_menu/other/barbarian_icon.png")
        if barbarian_icon_position:
            self.mouse.move(barbarian_icon_position[0], barbarian_icon_position[1])
        for _ in range(200):
            self.mouse.click()
        if army_camp_not_full_position:
            leave_position = army_camp_not_full_position[0] + 100, army_camp_not_full_position[1]
            self.mouse.move(leave_position[0], leave_position[1])
            self.mouse.safe_click()
        return Status.SUCCESS

    def find_village_to_attack(self):
        attack_position = self.vision.get_image_position("clash_of_clans_bot/images/attack_menu/other/attack.png")
        if attack_position:
            self.mouse.move(attack_position[0], attack_position[1])
            self.mouse.safe_click()
        return Status.SUCCESS