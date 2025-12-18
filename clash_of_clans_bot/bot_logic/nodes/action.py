import logging
from clash_of_clans_bot.bot_logic.nodes.node import Node
from clash_of_clans_bot.bot_logic.enums.status_enum import StatusEnum as Status

logger = logging.getLogger(__name__)


class Action(Node):
    def __init__(self, action_func, *args, **kwargs):
        self.action_func = action_func
        self.args = args
        self.kwargs = kwargs

    def tick(self, indent=0):
        indent_str = self._indent(indent)
        args_kwargs = self._format_args_kwargs(self.args, self.kwargs)
        
        if args_kwargs:
            logger.info(f"{indent_str}Action: {self.action_func.__name__}({args_kwargs})")
        else:
            logger.info(f"{indent_str}Action: {self.action_func.__name__}()")
        
        status = self.action_func(*self.args, **self.kwargs)
        
        logger.info(f"{indent_str}  └─ {self.action_func.__name__} -> {status.name}")
        return status

