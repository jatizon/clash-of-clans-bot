import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

logger = logging.getLogger(__name__)

class Sequence(Node):
    def __init__(self, children):
        self.children = children

    def run(self, indent=0):
        indent_str = self._indent(indent)
        logger.info(f"{indent_str}Sequence")
        for i, child in enumerate(self.children):
            status = child.run(indent + 1)
            if status != Status.SUCCESS:
                logger.info(f"{indent_str}Sequence -> {status.name} (stopped at child {i+1})")
                return status
        logger.info(f"{indent_str}Sequence -> SUCCESS")
        return Status.SUCCESS

