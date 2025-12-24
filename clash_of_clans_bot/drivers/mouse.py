import pyautogui
from clash_of_clans_bot.enums.status_enum import Status
import time


class Mouse:
    def __init__(self, human_clicker):
        self.hc = human_clicker

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

    def safe_click(self):
        self.click()
        time.sleep(0.5)

    def right_click(self):
        pyautogui.rightClick()

    def double_click(self):
        pyautogui.doubleClick()

    def scroll(self, dy):
        pyautogui.scroll(dy)

    def zoom_out(self):
        # For some reason, just scrolling 1000
        # doesn't work, so we scroll 100 10 times
        for _ in range(50):
            self.scroll(-100)
            
    def center_screen(self):
        self.zoom_out()
        self.move_to_center()
        # Hardcoded values used to center the screen
        screen_width, screen_height = pyautogui.size()
        self.drag_screen(int(0.3*screen_width), int(0.3*screen_height))
        self.drag_screen(-int(0.1*screen_width), -int(0.05*screen_height))
        time.sleep(0.5)