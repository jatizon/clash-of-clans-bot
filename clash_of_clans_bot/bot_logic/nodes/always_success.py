import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

logger = logging.getLogger(__name__)

class AlwaysSuccess(Node):
    def __init__(self, child):
        self.child = child
        self._child_running = False  # State: whether child is currently running
    
    def run(self, indent=0):
        indent_str = self._indent(indent)
        state_info = "state: child running" if self._child_running else "state: fresh"
        logger.info(f"{indent_str}AlwaysSuccess ({state_info})")
        
        if self._child_running:
            logger.info(f"{indent_str}  └─ Resuming child")
        else:
            logger.info(f"{indent_str}  └─ Executing child")
        
        status = self.child.run(indent + 1)  # Execute child but ignore its result
        logger.info(f"{indent_str}  └─ Child -> {status.name} (ignored)")
        
        if status == Status.RUNNING:
            self._child_running = True  # Save state
            logger.info(f"{indent_str}AlwaysSuccess -> RUNNING (child is running, state saved)")
            return Status.RUNNING
        else:
            self._child_running = False  # Reset state
            logger.info(f"{indent_str}AlwaysSuccess -> SUCCESS (state reset)")
            return Status.SUCCESS

