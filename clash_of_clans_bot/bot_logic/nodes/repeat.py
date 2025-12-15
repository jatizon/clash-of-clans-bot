import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.nodes.status import Status

logger = logging.getLogger(__name__)

class Repeat(Node):
    def __init__(self, child, times=None, stop_on_failure=False, stop_on_success=False):
        self.child = child
        self.times = times
        self.stop_on_failure = stop_on_failure
        self.stop_on_success = stop_on_success

    def run(self, indent=0):
        indent_str = self._indent(indent)
        stop_info = []
        if self.stop_on_failure:
            stop_info.append("stop_on_failure=True")
        if self.stop_on_success:
            stop_info.append("stop_on_success=True")
        stop_str = f", {', '.join(stop_info)}" if stop_info else ""
        logger.info(f"{indent_str}Repeat (times={self.times}{stop_str})")
        count = 0
        while self.times is None or count < self.times:
            logger.info(f"{indent_str}  └─ Iteration {count + 1}")
            status = self.child.run(indent + 2)
            logger.info(f"{indent_str}  └─ Iteration {count + 1} -> {status.name}")
            count += 1

            if status == Status.FAILURE and self.stop_on_failure:
                logger.info(f"{indent_str}Repeat -> FAILURE (stopped at iteration {count})")
                return Status.FAILURE
            if status == Status.SUCCESS and self.stop_on_success:
                logger.info(f"{indent_str}Repeat -> SUCCESS (stopped at iteration {count})")
                return Status.SUCCESS

        logger.info(f"{indent_str}Repeat -> SUCCESS (completed {count} iterations)")
        return Status.SUCCESS

