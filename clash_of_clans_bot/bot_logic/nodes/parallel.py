import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

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

    def run(self, indent=0):
        indent_str = self._indent(indent)
        logger.info(f"{indent_str}Parallel (policy={self.policy})")
        
        # Execute all children independently
        results = []
        for i, child in enumerate(self.children):
            logger.info(f"{indent_str}  └─ Executing child {i+1}/{len(self.children)}")
            status = child.run(indent + 1)
            results.append(status)
            logger.info(f"{indent_str}  └─ Child {i+1} -> {status.name}")
        
        # Evaluate results according to policy
        if self.policy == 'Sequence':
            # All must succeed
            for i, status in enumerate(results):
                if status != Status.SUCCESS:
                    logger.info(f"{indent_str}Parallel -> {status.name} (child {i+1} failed)")
                    return status
            logger.info(f"{indent_str}Parallel -> SUCCESS (all children succeeded)")
            return Status.SUCCESS
        else:  # Selector policy
            # At least one must succeed
            for i, status in enumerate(results):
                if status == Status.SUCCESS:
                    logger.info(f"{indent_str}Parallel -> SUCCESS (child {i+1} succeeded)")
                    return Status.SUCCESS
            logger.info(f"{indent_str}Parallel -> FAILURE (no children succeeded)")
            return Status.FAILURE

