import logging

from clash_of_clans_bot.enums.status_enum import Status
from clash_of_clans_bot.nodes.node import Node

logger = logging.getLogger(__name__)


class Action(Node):
    def __init__(self, action_func, *args, **kwargs):
        self.action_func = action_func
        self.args = args
        self.kwargs = kwargs

    def tick(self, path=None):
        if path is None:
            path = []
        
        args_kwargs = self._format_args_kwargs(self.args, self.kwargs)
        action_name = self.action_func.__name__
        if args_kwargs:
            action_name += f"({args_kwargs})"
        
        status = self.action_func(*self.args, **self.kwargs)
        
        logger.info(f"{action_name} -> {status.name}")
        return status

