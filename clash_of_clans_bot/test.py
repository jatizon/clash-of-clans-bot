import pyautogui
import time
from clash_of_clans_bot.drivers.mouse import Mouse
from clash_of_clans_bot.drivers.vision import Vision
from clash_of_clans_bot.controllers.main_controller import MainController
from pyclick import HumanClicker

human_clicker = HumanClicker()
mouse = Mouse(human_clicker)
vision = Vision(images_path="clash_of_clans_bot")
controller = MainController(mouse, vision)
controller.ui.click_button("images/buttons/home_village/shop.png")


