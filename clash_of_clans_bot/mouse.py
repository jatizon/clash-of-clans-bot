import pyautogui
import random
from clash_of_clans_bot.bot_logic.nodes.status import Status
import time
from pyclick import HumanClicker
from pathlib import Path
import os

class MouseWrapper:
    def __init__(self, human_clicker):
        self.hc = human_clicker
        # Get the base directory of the clash_of_clans_bot package
        self.base_dir = Path(__file__).parent.resolve()

    def move(self, x, y, movement_duration=0.1):
        self.hc.move((x, y), movement_duration)

    def move_relative(self, dx, dy, movement_duration=0.1):
        current_x, current_y = pyautogui.position()
        new_x = current_x + dx
        new_y = current_y + dy
        self.hc.move((new_x, new_y), movement_duration)

    def move_to_center(self, movement_duration=0.1):
        self.hc.move((pyautogui.size()[0] // 2, pyautogui.size()[1] // 2), movement_duration)
        return Status.SUCCESS

    def center_screen_clash(self):
        self.zoom_out()
        self.move_to_center()
        # Hardcoded values used to center the screen
        screen_width, screen_height = pyautogui.size()
        self.drag_screen(int(0.3*screen_width), int(0.3*screen_height))
        self.drag_screen(-int(0.1*screen_width), -int(0.05*screen_height))
        return Status.SUCCESS

    def hold_down(self, button='left'):
        pyautogui.mouseDown(button=button)

    def release(self, button='left'):
        pyautogui.mouseUp(button=button)

    def drag_screen(self, dx, dy, movement_duration=0.1):
        self.move_to_center()
        self.hold_down()
        self.move_relative(dx, dy, movement_duration)
        self.release()

    def click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def double_click(self):
        pyautogui.doubleClick()

    def zoom_out(self):
        # For some reason, just scrolling 1000
        # doesn't work, so we scroll 100 10 times
        for _ in range(10):
            pyautogui.scroll(-100)
        return Status.SUCCESS

    def _resolve_image_path(self, image_path):
        # Resolve relative to the clash_of_clans_bot package directory
        resolved_path = os.path.join(self.base_dir, image_path)
        return str(resolved_path)
    
    def _get_image_position(self, image_path, confidence):
        try:
            resolved_path = self._resolve_image_path(image_path)
            button_location = pyautogui.locateOnScreen(resolved_path, confidence=confidence)
            return pyautogui.center(button_location)
        except Exception:
            return None
        
    def check_image_exists(self, image_path, confidence=0.7, time_await=0.1):
        time.sleep(time_await)
        position = self._get_image_position(image_path, confidence)
        return Status.SUCCESS if position else Status.FAILURE

    def click_button(self, image_path, confidence=0.7, time_await=0.1, delta_x=0, delta_y=0):
        time.sleep(time_await)
        position = self._get_image_position(image_path, confidence)
        if position:
            self.move(position[0] + delta_x, position[1] + delta_y)
            self.click()
            time.sleep(1)
            return Status.SUCCESS
        else:
            return Status.FAILURE
        
    def deploy_troops(self):
        screen_width, screen_height = pyautogui.size()
        for _ in range(5):
            rand_x = random.randint(0, screen_width)
            rand_y = random.randint(0, screen_height)
            self.move(rand_x, rand_y, movement_duration=0.1)
            self.click()
        return Status.SUCCESS

Mouse = MouseWrapper

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)
