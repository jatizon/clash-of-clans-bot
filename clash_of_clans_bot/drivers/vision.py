import os
import pyautogui
import random

class Vision:
    def __init__(self, images_path):
        self.images_path = images_path
    
    def get_image_position(self, image_path, confidence=0.7):
        try:
            resolved_path = os.path.join(self.images_path, image_path)
            button_location = pyautogui.locateOnScreen(resolved_path, confidence=confidence)
            return pyautogui.center(button_location)
        except Exception:
            return None
        
    def is_image_on_screen(self, image_path, confidence=0.7):
        position = self.get_image_position(image_path, confidence)
        return True if position else False

    def random_point(self):
        screen_width, screen_height = pyautogui.size()
        return random.randint(0, screen_width), random.randint(0, screen_height)

