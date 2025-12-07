import pyautogui
import random
from btree import Status
import time

class Mouse:
    def __init__(self):
        pass

    def move(self, x, y, movement_duration=1, steps=10, randomness=10):
        current_x, current_y = pyautogui.position()
        duration = movement_duration if movement_duration is not None else self.movement_duration
        for i in range(1, steps + 1):
            interp_x = current_x + (x - current_x) * i / steps
            interp_y = current_y + (y - current_y) * i / steps
            rand_x = interp_x + random.randint(-randomness, randomness)
            rand_y = interp_y + random.randint(-randomness, randomness)
            pyautogui.moveTo(int(rand_x), int(rand_y), duration / steps)

    def click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def double_click(self):
        pyautogui.doubleClick()

    def _get_image_position(self, image_path, confidence):
        try:
            button_location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            return pyautogui.center(button_location)
        except Exception:
            return None
        
    def check_image_exists(self, image_path, confidence=0.7, time_await=1):
        time.sleep(time_await)
        position = self._get_image_position(image_path, confidence)
        return Status.SUCCESS if position else Status.FAILURE

    def click_button(self, image_path, confidence=0.7, time_await=1):
        time.sleep(time_await)
        position = self._get_image_position(image_path, confidence)
        if position:
            self.move(position[0], position[1])
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