import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

logger = logging.getLogger(__name__)

class Sequence(Node):
    def __init__(self, children):
        self.children = children
        self._current_index = 0  # State: which child we're currently executing
    
    def run(self, indent=0):
        indent_str = self._indent(indent)
        logger.info(f"{indent_str}Sequence ({len(self.children)} children, state: child {self._current_index + 1})")
        
        # Continue from where we left off
        for i in range(self._current_index, len(self.children)):
            child = self.children[i]
            logger.info(f"{indent_str}  └─ Executing child {i+1}/{len(self.children)}")
            status = child.run(indent + 1)
            
            if status == Status.RUNNING:
                self._current_index = i  # Save state: continue from this child next tick
                logger.info(f"{indent_str}Sequence -> RUNNING (child {i+1} is running, state saved)")
                return Status.RUNNING
            elif status != Status.SUCCESS:
                # Reset state on failure
                self._current_index = 0
                logger.info(f"{indent_str}Sequence -> {status.name} (stopped at child {i+1}, state reset)")
                return status
            
            logger.info(f"{indent_str}  └─ Child {i+1} -> SUCCESS")
            self._current_index = i + 1  # Move to next child
        
        # All children succeeded - reset state
        self._current_index = 0
        logger.info(f"{indent_str}Sequence -> SUCCESS (all children succeeded, state reset)")
        return Status.SUCCESS

