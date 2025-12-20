import logging
from clash_of_clans_bot.nodes.node import Node
from clash_of_clans_bot.enums.status_enum import StatusEnum as Status

logger = logging.getLogger(__name__)

class AlwaysSuccess(Node):
    def __init__(self, child):
        self.child = child
        self._child_running = False  # State: whether child is currently running
    
    def tick(self, path=None):
        if path is None:
            path = []
        
        current_path = path + ["AS"]
        
        status = self.child.tick(current_path)  # Execute child but ignore its result
        
        if status == Status.RUNNING:
            self._child_running = True  # Save state
            return Status.RUNNING
        else:
            self._child_running = False  # Reset state
            return Status.SUCCESS

