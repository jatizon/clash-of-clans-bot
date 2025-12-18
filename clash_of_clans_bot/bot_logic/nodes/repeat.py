import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.enums.status_enum import StatusEnum as Status

logger = logging.getLogger(__name__)

class Repeat(Node):
    def __init__(self, child, times=None, stop_on_failure=False, stop_on_success=False):
        self.child = child
        self.times = times
        self.stop_on_failure = stop_on_failure
        self.stop_on_success = stop_on_success
        self._current_iteration = 0  # State: current iteration count
        self._child_running = False  # State: whether child is currently running
    
    def tick(self, indent=0):
        indent_str = self._indent(indent)
        stop_info = []
        if self.stop_on_failure:
            stop_info.append("stop_on_failure=True")
        if self.stop_on_success:
            stop_info.append("stop_on_success=True")
        stop_str = f", {', '.join(stop_info)}" if stop_info else ""
        state_info = f"state: iteration {self._current_iteration + 1}" if self._child_running else f"state: iteration {self._current_iteration + 1} (fresh)"
        logger.info(f"{indent_str}Repeat (times={self.times}{stop_str}, {state_info})")
        
        # Continue iterations until limit or stop condition
        while self.times is None or self._current_iteration < self.times:
            # If child was running, continue from same iteration
            if not self._child_running:
                self._current_iteration += 1
            
            logger.info(f"{indent_str}  └─ Iteration {self._current_iteration}")
            status = self.child.tick(indent + 2)
            logger.info(f"{indent_str}  └─ Iteration {self._current_iteration} -> {status.name}")
            
            if status == Status.RUNNING:
                self._child_running = True  # Save state: child is running
                logger.info(f"{indent_str}Repeat -> RUNNING (child is running at iteration {self._current_iteration}, state saved)")
                return Status.RUNNING
            
            # Child completed (SUCCESS or FAILURE)
            self._child_running = False  # Reset child running state
            
            if status == Status.FAILURE and self.stop_on_failure:
                self._current_iteration = 0  # Reset state
                logger.info(f"{indent_str}Repeat -> FAILURE (stopped at iteration {self._current_iteration}, state reset)")
                return Status.FAILURE
            
            if status == Status.SUCCESS and self.stop_on_success:
                self._current_iteration = 0  # Reset state
                logger.info(f"{indent_str}Repeat -> SUCCESS (stopped at iteration {self._current_iteration}, state reset)")
                return Status.SUCCESS
            
            # Continue to next iteration if not stopped
        
        # Completed all iterations - reset state
        completed = self._current_iteration
        self._current_iteration = 0
        self._child_running = False
        logger.info(f"{indent_str}Repeat -> SUCCESS (completed {completed} iterations, state reset)")
        return Status.SUCCESS

