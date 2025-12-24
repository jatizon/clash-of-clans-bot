import random
from re import T

import pyautogui


class Vision:
    def __init__(self, images_path=None):
        self.images_path = images_path

    def get_image_position(self, image_path, confidence=0.9, grayscale=True):
        try:
            button_location = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=grayscale)
            return pyautogui.center(button_location)
        except Exception:
            return None

    def get_image_position_all(self, image_path, confidence=0.9):
        try:
            button_locations = pyautogui.locateAllOnScreen(image_path, confidence=confidence)
            return [pyautogui.center(button_location) for button_location in button_locations]
        except Exception:
            return []

    def _matrix_has_color(self, s, x, y, color, pixel_matrix_size, tolerance):
        for i in range(pixel_matrix_size[0]):
            for j in range(pixel_matrix_size[1]):
                for k in range(3):
                    if abs(s.getpixel((x + i, y + j))[k] - color[k]) > tolerance[k]:
                        return False
        return True
    
    def get_color_position(self, color, pixel_matrix_size=(10, 10), tolerance=(20, 20, 20)):
        s = pyautogui.screenshot()
        for x in range(s.width-pixel_matrix_size[0]):
            for y in range(s.height-pixel_matrix_size[1]):
                found = self._matrix_has_color(s, x, y, color, pixel_matrix_size, tolerance)
                if found:
                    return (x, y)
        return None

    def is_image_on_screen(self, image_path, confidence=0.9, grayscale=True):
        position = self.get_image_position(image_path, confidence, grayscale)
        return True if position else False

    def random_point(self, percentage_of_screen=0.70):
        screen_width, screen_height = pyautogui.size()
        start = (1-percentage_of_screen)/2
        end = (1+percentage_of_screen)/2
        return random.randint(int(screen_width*start), int(screen_width*end)), random.randint(int(screen_height*start), int(screen_height*end))

a = Vision()
print(a.is_image_on_screen("clash_of_clans_bot/images/profile/other/claim_reward.png", grayscale=False))