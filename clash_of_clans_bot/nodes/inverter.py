import logging

from clash_of_clans_bot.enums.status_enum import Status
from clash_of_clans_bot.nodes.node import Node

logger = logging.getLogger(__name__)

class Inverter(Node):
    def __init__(self, child):
        self.child = child
        self._child_running = False  # State: whether child is currently running
    
    def tick(self, path=None):
        if path is None:
            path = []
        
        current_path = path + ["Inv"]
        
        status = self.child.tick(current_path)
        
        if status == Status.SUCCESS:
            self._child_running = False  # Reset state
            return Status.FAILURE
        elif status == Status.FAILURE:
            self._child_running = False  # Reset state
            return Status.SUCCESS
        else:  # RUNNING
            self._child_running = True  # Save state
            return Status.RUNNING

