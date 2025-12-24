import logging

from clash_of_clans_bot.enums.status_enum import Status
from clash_of_clans_bot.nodes.node import Node

logger = logging.getLogger(__name__)

class Selector(Node):
    def __init__(self, children):
        self.children = children
        self._running_child_index = None  # State: which child is currently running
    
    def tick(self, path=None):
        if path is None:
            path = []
        
        current_path = path + ["Sel"]
        
        # If we have a running child, continue from there
        start_index = self._running_child_index if self._running_child_index is not None else 0
        
        for i in range(start_index, len(self.children)):
            child = self.children[i]
            status = child.tick(current_path)
            
            if status == Status.SUCCESS:
                # Reset state on success
                self._running_child_index = None
                return Status.SUCCESS
            elif status == Status.RUNNING:
                self._running_child_index = i  # Save state: this child is running
                return Status.RUNNING
            else:  # FAILURE
                # Continue to next child, don't save state for failures
                pass
        
        # All children failed - reset state
        self._running_child_index = None
        return Status.FAILURE

