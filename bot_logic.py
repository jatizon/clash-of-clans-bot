import logging
from btree import Status
from btree import Sequence
from btree import Action
from mouse import Mouse

logging.basicConfig(level=logging.INFO, format='%(message)s')

mouse = Mouse()

def click_button(mouse, image_path):
    mouse_click_status = mouse.click_button(image_path)
    return Status.SUCCESS if mouse_click_status == Status.SUCCESS else Status.FAILURE

def attack(mouse):
    return click_button(mouse, "buttons/attack.png")

def open_shop(mouse):
    return click_button(mouse, "buttons/shop.png")

btree = Sequence([
    Action(attack, mouse),
    Action(open_shop, mouse),
    Action(open_shop, mouse),
])

btree.run()