import logging

from enum import Enum

# Configure logger
logger = logging.getLogger(__name__)

class Status(Enum):
    SUCCESS = 1
    FAILURE = 2
    RUNNING = 3


class Node:
    def tick(self):
        raise NotImplementedError

class Action(Node):
    def __init__(self, action_func, *args, **kwargs):
        self.action_func = action_func
        self.args = args
        self.kwargs = kwargs

    def tick(self):
        logger.info(f"Action: {self.action_func.__name__}")
        status = self.action_func(*self.args, **self.kwargs)
        logger.info(f"Action: {self.action_func.__name__} -> {status.name}")
        return status

class Sequence(Node):
    def __init__(self, children):
        self.children = children

    def tick(self):
        logger.info("Sequence")
        for child in self.children:
            status = child.tick()
            if status != Status.SUCCESS:
                logger.info(f"Sequence -> {status.name}")
                return status
        logger.info("Sequence -> SUCCESS")
        return Status.SUCCESS

class Selector(Node):
    def __init__(self, children):
        self.children = children

    def tick(self):
        logger.info("Selector")
        for child in self.children:
            status = child.tick()
            if status == Status.SUCCESS:
                logger.info("Selector -> SUCCESS")
                return Status.SUCCESS
        logger.info("Selector -> FAILURE")
        return Status.FAILURE
    
class Repeat(Node):
    def __init__(self, child, times=None, stop_on_failure=False, stop_on_success=False):
        self.child = child
        self.times = times
        self.stop_on_failure = stop_on_failure
        self.stop_on_success = stop_on_success

    def tick(self):
        logger.info(f"Repeat times={self.times}")
        count = 0
        while self.times is None or count < self.times:
            logger.info(f"Repeat iteration {count + 1}")
            status = self.child.tick()
            logger.info(f"Repeat iteration {count + 1} -> child status: {status.name}")
            count += 1

            if status == Status.FAILURE and self.stop_on_failure:
                logger.info(f"Repeat -> stopping on FAILURE at iteration {count}")
                return Status.FAILURE
            if status == Status.SUCCESS and self.stop_on_success:
                logger.info(f"Repeat -> stopping on SUCCESS at iteration {count}")
                return Status.SUCCESS

        logger.info(f"Repeat -> completed {count} iterations")
        return Status.SUCCESS if self.stop_on_success else Status.FAILURE
