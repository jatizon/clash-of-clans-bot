from clash_of_clans_bot.enums.status_enum import Status


class ProfileController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision

    def claim_reward(self):
        CLAIM_ACHIEVEMENT_REWARDS_position = self.vision.get_image_position("clash_of_clans_bot/images/profile/other/claim_reward.png")
        if CLAIM_ACHIEVEMENT_REWARDS_position:
            self.mouse.move(CLAIM_ACHIEVEMENT_REWARDS_position[0], CLAIM_ACHIEVEMENT_REWARDS_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def close_profile(self):
        close_position = self.vision.get_image_position("clash_of_clans_bot/images/profile/other/close.png")
        if close_position:
            self.mouse.move(close_position[0], close_position[1])
            self.mouse.click()
        return Status.SUCCESS