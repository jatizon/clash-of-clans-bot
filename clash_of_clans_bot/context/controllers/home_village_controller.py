from clash_of_clans_bot.behaviors.collect_resources import CollectResourcesBehavior
from clash_of_clans_bot.enums.status_enum import StatusEnum as Status

class HomeVillageController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision

    def try_collect_resources(self):
        gold_position = self.vision.get_image_position("images/home_village/other/gold_to_collect.png")
        if gold_position:
            self.mouse.move(gold_position[0], gold_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def has_achievements(self):
        return self.vision.get_image_position("images/home_village/other/achievements.png")

    def open_profile(self):
        profile_position = self.vision.get_image_position("images/home_village/other/profile.png")
        if profile_position:
            self.mouse.move(profile_position[0], profile_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def has_builder(self):
        return not self.vision.is_image_on_screen("images/home_village/other/no_builder.png")