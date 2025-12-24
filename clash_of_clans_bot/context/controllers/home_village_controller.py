from clash_of_clans_bot.enums.status_enum import Status
import random
import time

class HomeVillageController:
    def __init__(self, mouse, vision):
        self.mouse = mouse
        self.vision = vision

    def try_collect_resources(self):
        gold_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/gold_to_collect.png")
        elixir_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/elixir_to_collect.png")
        # dark_elixir_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/dark_elixir_to_collect.png")
        if gold_position:
            self.mouse.move(gold_position[0], gold_position[1])
            self.mouse.click()
        if elixir_position:
            self.mouse.move(elixir_position[0], elixir_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def check_has_achievements(self):
        achievements_on_screen = self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/has_achievements.png")
        if achievements_on_screen:
            return Status.SUCCESS
        return Status.FAILURE

    def open_profile(self):
        profile_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/profile.png")
        if profile_position:
            self.mouse.move(profile_position[0], profile_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def check_has_builder(self):
        has_no_builder = self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/no_builder.png")
        return Status.SUCCESS if not has_no_builder else Status.FAILURE

    def open_suggested_upgrades(self):
        builder_icon_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/builder.png")
        if builder_icon_position:
            self.mouse.move(builder_icon_position[0], builder_icon_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def choose_suggested_upgrade(self):
        suggested_upgrades_header_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/suggested_upgrades.png")
        if suggested_upgrades_header_position:
            self.mouse.move(suggested_upgrades_header_position[0], suggested_upgrades_header_position[1])
            # Scroll down random amount
            scroll_amount = random.randint(0, 100)
            for _ in range(scroll_amount):
                self.mouse.scroll(-1)
            time.sleep(0.2)
        gold_upgrade_positions = self.vision.get_image_position_all("clash_of_clans_bot/images/home_village/other/suggested_upgrade_gold.png")
        elixir_upgrade_positions = self.vision.get_image_position_all("clash_of_clans_bot/images/home_village/other/suggested_upgrade_elixir.png")
        free_upgrade_positions = self.vision.get_image_position_all("clash_of_clans_bot/images/home_village/other/suggested_upgrade_free.png")
        gems_upgrade_positions = self.vision.get_image_position_all("clash_of_clans_bot/images/home_village/other/suggested_upgrade_gems.png")
        upgrade_positions = gold_upgrade_positions + elixir_upgrade_positions + free_upgrade_positions + gems_upgrade_positions
        if upgrade_positions:
            upgrade_position = random.choice(upgrade_positions)
        else:
            upgrade_position = None
        upgrade_button_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/upgrade.png")
        if upgrade_button_position:
            self.mouse.move(upgrade_button_position[0], upgrade_button_position[1])
            self.mouse.click()
            return Status.SUCCESS
        if upgrade_position:
            self.mouse.move(upgrade_position[0], upgrade_position[1])
            self.mouse.click()
        return Status.RUNNING

    def try_build_new(self):
        build_new_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/confirm_new_building.png")
        if build_new_position:
            self.mouse.move(build_new_position[0], build_new_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def check_no_resources(self):
        is_on_screen = self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/no_resources.png")
        return Status.SUCCESS if is_on_screen else Status.FAILURE

    def close_no_resources_popup(self):
        close_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/close_new_building_popup.png")
        if close_position:
            self.mouse.move(close_position[0], close_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def unselect_building(self):
        unselect_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/neutral_click.png")
        if unselect_position:
            unselect_position = (unselect_position[0], unselect_position[1])
            self.mouse.move(unselect_position[0], unselect_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def center_screen(self):
        self.mouse.center_screen()
        return Status.SUCCESS

    def start_attack(self):
        attack_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/attack.png")
        print(attack_position)
        find_match_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/find_match.png")
        if attack_position:
            self.mouse.move(attack_position[0], attack_position[1])
            self.mouse.safe_click()
        find_match_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/find_match.png")
        if find_match_position:
            self.mouse.move(find_match_position[0], find_match_position[1])
            self.mouse.safe_click()
        return Status.SUCCESS

    def has_low_resources(self):
        gold_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/gold_almost_full.png", grayscale=False)
        elixir_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/elixir_almost_full.png", grayscale=False)
        return Status.FAILURE if gold_position and elixir_position else Status.SUCCESS