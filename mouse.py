import pyautogui
import random
from btree import Status

class Mouse:
    def __init__(self, movement_duration=1, steps=10, randomness=10, confidence=0.7):
        self.movement_duration = movement_duration
        self.steps = steps
        self.randomness = randomness
        self.confidence = confidence

    def move(self, x, y):
        current_x, current_y = pyautogui.position()
        for i in range(1, self.steps + 1):
            interp_x = current_x + (x - current_x) * i / self.steps
            interp_y = current_y + (y - current_y) * i / self.steps
            rand_x = interp_x + random.randint(-self.randomness, self.randomness)
            rand_y = interp_y + random.randint(-self.randomness, self.randomness)
            pyautogui.moveTo(int(rand_x), int(rand_y), self.movement_duration / self.steps)

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
        except:
            return None
    
    def click_button(self, image_path):
        position = self._get_image_position(image_path, self.confidence)
        if position:
            self.move(position[0], position[1])
            self.click()
            return Status.SUCCESS
        else:
            return Status.FAILURE