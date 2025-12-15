import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

logger = logging.getLogger(__name__)

class Inverter(Node):
    def __init__(self, child):
        self.child = child

    def run(self, indent=0):
        indent_str = self._indent(indent)
        logger.info(f"{indent_str}Inverter")
        status = self.child.run(indent + 1)
        
        if status == Status.SUCCESS:
            logger.info(f"{indent_str}Inverter -> FAILURE (inverted SUCCESS)")
            return Status.FAILURE
        elif status == Status.FAILURE:
            logger.info(f"{indent_str}Inverter -> SUCCESS (inverted FAILURE)")
            return Status.SUCCESS
        else:  # RUNNING
            logger.info(f"{indent_str}Inverter -> RUNNING")
            return Status.RUNNING

