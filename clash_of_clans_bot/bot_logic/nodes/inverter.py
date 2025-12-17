import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

logger = logging.getLogger(__name__)

class Inverter(Node):
    def __init__(self, child):
        self.child = child
        self._child_running = False  # State: whether child is currently running
    
    def run(self, indent=0):
        indent_str = self._indent(indent)
        state_info = "state: child running" if self._child_running else "state: fresh"
        logger.info(f"{indent_str}Inverter ({state_info})")
        
        if self._child_running:
            logger.info(f"{indent_str}  └─ Resuming child")
        else:
            logger.info(f"{indent_str}  └─ Executing child")
        
        status = self.child.run(indent + 1)
        logger.info(f"{indent_str}  └─ Child -> {status.name}")
        
        if status == Status.SUCCESS:
            self._child_running = False  # Reset state
            logger.info(f"{indent_str}Inverter -> FAILURE (inverted SUCCESS, state reset)")
            return Status.FAILURE
        elif status == Status.FAILURE:
            self._child_running = False  # Reset state
            logger.info(f"{indent_str}Inverter -> SUCCESS (inverted FAILURE, state reset)")
            return Status.SUCCESS
        else:  # RUNNING
            self._child_running = True  # Save state
            logger.info(f"{indent_str}Inverter -> RUNNING (child is running, state saved)")
            return Status.RUNNING

