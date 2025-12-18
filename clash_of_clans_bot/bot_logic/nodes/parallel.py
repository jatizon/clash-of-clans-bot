import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.enums.status_enum import StatusEnum as Status

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
    
    def tick(self, indent=0):
        indent_str = self._indent(indent)
        state_info = "state: resuming" if self._child_results is not None else "state: fresh"
        logger.info(f"{indent_str}Parallel (policy={self.policy}, {len(self.children)} children, {state_info})")
        
        # Initialize or reuse results
        if self._child_results is None:
            self._child_results = [None] * len(self.children)
        
        # Execute all children independently (only re-execute if not RUNNING)
        for i, child in enumerate(self.children):
            # If child was RUNNING, continue from there; otherwise execute fresh
            if self._child_results[i] == Status.RUNNING:
                logger.info(f"{indent_str}  └─ Resuming child {i+1}/{len(self.children)}")
            else:
                logger.info(f"{indent_str}  └─ Executing child {i+1}/{len(self.children)}")
            
            status = child.tick(indent + 1)
            self._child_results[i] = status
            logger.info(f"{indent_str}  └─ Child {i+1} -> {status.name}")
        
        # Evaluate results according to policy
        if self.policy == 'Sequence':
            # All must succeed
            # Check for failures first (they take priority)
            for i, status in enumerate(self._child_results):
                if status == Status.FAILURE:
                    self._child_results = None  # Reset state
                    logger.info(f"{indent_str}Parallel -> FAILURE (child {i+1} failed, state reset)")
                    return Status.FAILURE
            # Then check for running
            for i, status in enumerate(self._child_results):
                if status == Status.RUNNING:
                    logger.info(f"{indent_str}Parallel -> RUNNING (child {i+1} is running, state saved)")
                    return Status.RUNNING
            # All succeeded - reset state
            self._child_results = None
            logger.info(f"{indent_str}Parallel -> SUCCESS (all children succeeded, state reset)")
            return Status.SUCCESS
        else:  # Selector policy
            # At least one must succeed
            # Check for success first
            for i, status in enumerate(self._child_results):
                if status == Status.SUCCESS:
                    self._child_results = None  # Reset state
                    logger.info(f"{indent_str}Parallel -> SUCCESS (child {i+1} succeeded, state reset)")
                    return Status.SUCCESS
            # Then check for running
            for i, status in enumerate(self._child_results):
                if status == Status.RUNNING:
                    logger.info(f"{indent_str}Parallel -> RUNNING (child {i+1} is running, state saved)")
                    return Status.RUNNING
            # All failed - reset state
            self._child_results = None
            logger.info(f"{indent_str}Parallel -> FAILURE (no children succeeded, state reset)")
            return Status.FAILURE

