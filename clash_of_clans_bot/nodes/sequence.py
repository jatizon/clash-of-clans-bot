import logging

from clash_of_clans_bot.enums.status_enum import Status
from clash_of_clans_bot.nodes.node import Node

logger = logging.getLogger(__name__)

class Sequence(Node):
    def __init__(self, children):
        self.children = children
        self._current_index = 0  # State: which child we're currently executing
    
    def tick(self, path=None):
        if path is None:
            path = []
        
        current_path = path + ["Seq"]
        
        # Continue from where we left off
        for i in range(self._current_index, len(self.children)):
            child = self.children[i]
            status = child.tick(current_path)
            
            if status == Status.RUNNING:
                self._current_index = i  # Save state: continue from this child next tick
                return Status.RUNNING
            elif status != Status.SUCCESS:
                # Reset state on failure
                self._current_index = 0
                return status
            
            self._current_index = i + 1  # Move to next child
        
        # All children succeeded - reset state
        self._current_index = 0
        return Status.SUCCESS

