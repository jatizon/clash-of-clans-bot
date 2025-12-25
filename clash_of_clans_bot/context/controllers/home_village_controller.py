from clash_of_clans_bot.enums.status_enum import Status
import random
import time
import os


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

    def check_has_lab(self):
        has_no_lab = self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/no_lab.png")
        return Status.SUCCESS if not has_no_lab else Status.FAILURE

    def choose_builder_upgrade(self):
        icon_path = "clash_of_clans_bot/images/home_village/other/builder.png"
        icon_position = self.vision.get_image_position(icon_path)
        if icon_position:
            self.mouse.move(icon_position[0], icon_position[1])
            self.mouse.safe_click()
        all_upgrades_completed = self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/all_upgrades_completed.png")
        if all_upgrades_completed:
            return Status.FAILURE
        suggested_upgrades_header_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/suggested_upgrades.png")
        if suggested_upgrades_header_position:
            self.mouse.move(suggested_upgrades_header_position[0], suggested_upgrades_header_position[1])
            # Scroll down random amount
            scroll_amount = random.randint(0, 100)
            for _ in range(scroll_amount):
                self.mouse.scroll(-1)
            time.sleep(0.2)
        upgrade_types = [
            "suggested_upgrade_gold",
            "suggested_upgrade_elixir",
            "suggested_upgrade_free",
            "suggested_upgrade_gems"
        ]
        upgrade_positions = []
        for upgrade_type in upgrade_types:
            positions = self.vision.get_image_position_all(f"clash_of_clans_bot/images/home_village/other/{upgrade_type}.png")
            upgrade_positions.extend(positions)
        upgrade_position = random.choice(upgrade_positions) if upgrade_positions else None
        if upgrade_position:
            self.mouse.move(upgrade_position[0], upgrade_position[1])
            self.mouse.safe_click()
        upgrade_button_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/upgrade.png")
        if upgrade_button_position:
            self.mouse.move(upgrade_button_position[0], upgrade_button_position[1])
            self.mouse.safe_click()
            return Status.SUCCESS
        return Status.RUNNING

    def choose_lab_upgrade(self):
        icon_path = "clash_of_clans_bot/images/home_village/other/lab.png"
        icon_position = self.vision.get_image_position(icon_path)
        if icon_position:
            self.mouse.move(icon_position[0], icon_position[1])
            self.mouse.safe_click()
        all_upgrades_completed = self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/all_upgrades_completed.png")
        if all_upgrades_completed:
            return Status.FAILURE
        suggested_upgrades_header_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/suggested_upgrades.png")
        if suggested_upgrades_header_position:
            self.mouse.move(suggested_upgrades_header_position[0], suggested_upgrades_header_position[1])
            # Scroll down random amount
            scroll_amount = random.randint(0, 100)
            for _ in range(scroll_amount):
                self.mouse.scroll(-1)
            time.sleep(0.2)
        upgrade_types = [
            "suggested_upgrade_gold",
            "suggested_upgrade_elixir",
            "suggested_upgrade_free",
            "suggested_upgrade_gems"
        ]
        upgrade_positions = []
        for upgrade_type in upgrade_types:
            positions = self.vision.get_image_position_all(f"clash_of_clans_bot/images/home_village/other/{upgrade_type}.png")
            upgrade_positions.extend(positions)
        upgrade_position = random.choice(upgrade_positions) if upgrade_positions else None
        if upgrade_position:
            self.mouse.move(upgrade_position[0], upgrade_position[1])
            self.mouse.safe_click()
        upgrade_button_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/upgrade.png")
        if upgrade_button_position:
            self.mouse.move(upgrade_button_position[0], upgrade_button_position[1])
            self.mouse.safe_click()
            return Status.SUCCESS
        return Status.RUNNING

    def try_build_new(self):
        build_new_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/confirm_new_building.png")
        if build_new_position:
            self.mouse.move(build_new_position[0], build_new_position[1])
            self.mouse.click()
        return Status.SUCCESS

    def check_no_resources(self):
        is_on_screen = (
            self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/no_resources.png")
            or self.vision.is_image_on_screen("clash_of_clans_bot/images/home_village/other/enter_shop.png")
        )
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

    def has_obstacles(self):
        for image in os.listdir("clash_of_clans_bot/images/home_village/other/obstacles"):
            image_path = os.path.join("clash_of_clans_bot/images/home_village/other/obstacles", image)
            obstacle_position = self.vision.get_image_position(image_path)
            if obstacle_position:
                return Status.SUCCESS
        return Status.FAILURE

    def remove_obstacle(self):
        for image in os.listdir("clash_of_clans_bot/images/home_village/other/obstacles"):
            image_path = os.path.join("clash_of_clans_bot/images/home_village/other/obstacles", image)
            obstacle_position = self.vision.get_image_position(image_path, confidence=0.8)
            if obstacle_position:
                self.mouse.move(obstacle_position[0], obstacle_position[1])
                self.mouse.safe_click()
            remove_obstacle_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/remove_obstacle.png")
            if remove_obstacle_position:
                self.mouse.move(remove_obstacle_position[0], remove_obstacle_position[1])
                self.mouse.click()
            no_resources_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/no_resources.png")
            if no_resources_position:
                self.mouse.move(no_resources_position[0], no_resources_position[1])
                self.mouse.safe_click()
            close_position = self.vision.get_image_position("clash_of_clans_bot/images/home_village/other/close_new_build_popup.png")
            if close_position:
                self.mouse.move(close_position[0], close_position[1])
                self.mouse.click()
        return Status.SUCCESS