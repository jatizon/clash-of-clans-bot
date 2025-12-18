import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.enums.status_enum import StatusEnum as Status

logger = logging.getLogger(__name__)

class Selector(Node):
    def __init__(self, children):
        self.children = children
        self._running_child_index = None  # State: which child is currently running
    
    def tick(self, indent=0):
        indent_str = self._indent(indent)
        state_info = f"state: child {self._running_child_index + 1} running" if self._running_child_index is not None else "state: fresh"
        logger.info(f"{indent_str}Selector ({len(self.children)} children, {state_info})")
        
        # If we have a running child, continue from there
        start_index = self._running_child_index if self._running_child_index is not None else 0
        
        for i in range(start_index, len(self.children)):
            child = self.children[i]
            logger.info(f"{indent_str}  └─ Executing child {i+1}/{len(self.children)}")
            status = child.tick(indent + 1)
            
            if status == Status.SUCCESS:
                # Reset state on success
                self._running_child_index = None
                logger.info(f"{indent_str}  └─ Child {i+1} -> SUCCESS")
                logger.info(f"{indent_str}Selector -> SUCCESS (succeeded at child {i+1}, state reset)")
                return Status.SUCCESS
            elif status == Status.RUNNING:
                self._running_child_index = i  # Save state: this child is running
                logger.info(f"{indent_str}  └─ Child {i+1} -> RUNNING")
                logger.info(f"{indent_str}Selector -> RUNNING (child {i+1} is running, state saved)")
                return Status.RUNNING
            else:  # FAILURE
                logger.info(f"{indent_str}  └─ Child {i+1} -> FAILURE")
                # Continue to next child, don't save state for failures
        
        # All children failed - reset state
        self._running_child_index = None
        logger.info(f"{indent_str}Selector -> FAILURE (no children succeeded, state reset)")
        return Status.FAILURE

