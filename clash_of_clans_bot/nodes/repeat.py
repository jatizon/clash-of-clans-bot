import logging

from clash_of_clans_bot.enums.status_enum import Status
from clash_of_clans_bot.nodes.node import Node

logger = logging.getLogger(__name__)

class Repeat(Node):
    def __init__(self, child, times=None, stop_on_failure=False, stop_on_success=False):
        self.child = child
        self.times = times
        self.stop_on_failure = stop_on_failure
        self.stop_on_success = stop_on_success
        self._current_iteration = 0  # State: current iteration count
        self._child_running = False  # State: whether child is currently running
    
    def tick(self, path=None):
        if path is None:
            path = []
        
        current_path = path + ["Rep"]
        
        # Continue iterations until limit or stop condition
        while self.times is None or self._current_iteration < self.times:
            # If child was running, continue from same iteration
            if not self._child_running:
                self._current_iteration += 1
            
            status = self.child.tick(current_path)
            
            if status == Status.RUNNING:
                self._child_running = True  # Save state: child is running
                return Status.RUNNING
            
            # Child completed (SUCCESS or FAILURE)
            self._child_running = False  # Reset child running state
            
            if status == Status.FAILURE and self.stop_on_failure:
                self._current_iteration = 0  # Reset state
                return Status.FAILURE
            
            if status == Status.SUCCESS and self.stop_on_success:
                self._current_iteration = 0  # Reset state
                return Status.SUCCESS
            
            # Continue to next iteration if not stopped
        
        # Completed all iterations - reset state
        completed = self._current_iteration
        self._current_iteration = 0
        self._child_running = False
        return Status.SUCCESS

