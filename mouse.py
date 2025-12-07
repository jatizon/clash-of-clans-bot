import pyautogui
import random

class Mouse:
    def __init__(self, steps=10, randomness=10):
        self.steps = steps
        self.randomness = randomness

    def move(self, x, y, duration):
        current_x, current_y = pyautogui.position()
        for i in range(1, self.steps + 1):
            interp_x = current_x + (x - current_x) * i / self.steps
            interp_y = current_y + (y - current_y) * i / self.steps
            rand_x = interp_x + random.randint(-self.randomness, self.randomness)
            rand_y = interp_y + random.randint(-self.randomness, self.randomness)
            pyautogui.moveTo(int(rand_x), int(rand_y), duration / self.steps)

    def click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def double_click(self):
        pyautogui.doubleClick()
