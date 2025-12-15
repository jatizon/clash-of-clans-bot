import pyautogui
import time
from clash_of_clans_bot.mouse import MouseWrapper
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = MouseWrapper(human_clicker)
mouse.click_button("buttons/shop.png")


