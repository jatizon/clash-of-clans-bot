from clash_of_clans_bot.enums.status_enum import Status


class AttackController():
    def __init__(self, mouse, vision):
        self._mouse = mouse
        self._vision = vision

    def on_attack_state(self):
        return Status.SUCCESS

    def deploy_troops(self, count=30):
        for _ in range(count):
            x, y = self._vision.random_point()
            self._mouse.move(x, y, movement_duration=0.1)
            self._mouse.click()
        return Status.SUCCESS

    def did_attack_end(self):
        return_home_position = self._vision.get_image_position("clash_of_clans_bot/images/attack/other/return_home.png")
        return Status.SUCCESS if return_home_position else Status.FAILURE

    def go_back_to_home_village(self):
        return_home_position = self._vision.get_image_position("clash_of_clans_bot/images/attack/other/return_home.png")
        if return_home_position:
            self._mouse.move(return_home_position[0], return_home_position[1])
            self._mouse.click()
        return Status.SUCCESS

    def select_troop(self):
        troop_position = self._vision.get_image_position("clash_of_clans_bot/images/attack/other/barbarian_icon.png")
        if troop_position:
            self._mouse.move(troop_position[0], troop_position[1])
            self._mouse.click()
        return Status.SUCCESS