import logging

from clash_of_clans_bot.enums.status_enum import Status
from clash_of_clans_bot.nodes.node import Node

logger = logging.getLogger(__name__)

class Parallel(Node):
    def __init__(self, children, policy='Sequence'):
        """
        policy: 'Sequence' or 'Selector'
        - 'Sequence': All children must succeed (returns FAILURE if any fails)
        - 'Selector': At least one child must succeed (returns SUCCESS if any succeeds)
        """
        self.children = children
        self.policy = policy
        self._child_results = None  # State: results from previous tick (None = fresh start)
    
    def tick(self, path=None):
        if path is None:
            path = []
        
        current_path = path + ["Par"]
        
        # Initialize or reuse results
        if self._child_results is None:
            self._child_results = [None] * len(self.children)
        
        # Execute all children independently (only re-execute if not RUNNING)
        for i, child in enumerate(self.children):
            # If child was RUNNING, continue from there; otherwise execute fresh
            status = child.tick(current_path)
            self._child_results[i] = status
        
        # Evaluate results according to policy
        if self.policy == 'Sequence':
            # All must succeed
            # Check for failures first (they take priority)
            for i, status in enumerate(self._child_results):
                if status == Status.FAILURE:
                    self._child_results = None  # Reset state
                    return Status.FAILURE
            # Then check for running
            for i, status in enumerate(self._child_results):
                if status == Status.RUNNING:
                    return Status.RUNNING
            # All succeeded - reset state
            self._child_results = None
            return Status.SUCCESS
        else:  # Selector policy
            # At least one must succeed
            # Check for success first
            for i, status in enumerate(self._child_results):
                if status == Status.SUCCESS:
                    self._child_results = None  # Reset state
                    return Status.SUCCESS
            # Then check for running
            for i, status in enumerate(self._child_results):
                if status == Status.RUNNING:
                    return Status.RUNNING
            # All failed - reset state
            self._child_results = None
            return Status.FAILURE

