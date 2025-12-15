import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

logger = logging.getLogger(__name__)

class AlwaysFailure(Node):
    def __init__(self, child):
        self.child = child

    def run(self, indent=0):
        indent_str = self._indent(indent)
        logger.info(f"{indent_str}AlwaysFailure")
        self.child.run(indent + 1)  # Execute child but ignore its result
        logger.info(f"{indent_str}AlwaysFailure -> FAILURE")
        return Status.FAILURE

