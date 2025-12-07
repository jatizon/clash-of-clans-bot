from enum import Enum
import logging

# Configure logger
logger = logging.getLogger(__name__)

class Status(Enum):
    SUCCESS = 1
    FAILURE = 2
    RUNNING = 3


class Node:
    def run(self):
        raise NotImplementedError

class Action(Node):
    def __init__(self, action_func, *args):
        self.action_func = action_func
        self.args = args

    def run(self):
        logger.info(f"Action: {self.action_func.__name__}")
        status = self.action_func(*self.args)
        logger.info(f"Action: {self.action_func.__name__} -> {status.name}")
        return status

class Sequence(Node):
    def __init__(self, children):
        self.children = children

    def run(self):
        logger.info("Sequence")
        for child in self.children:
            status = child.run()
            if status != Status.SUCCESS:
                logger.info(f"Sequence -> {status.name}")
                return status
        logger.info("Sequence -> SUCCESS")
        return Status.SUCCESS

class Selector(Node):
    def __init__(self, children):
        self.children = children

    def run(self):
        logger.info("Selector")
        for child in self.children:
            status = child.run()
            if status == Status.SUCCESS:
                logger.info("Selector -> SUCCESS")
                return Status.SUCCESS
        logger.info("Selector -> FAILURE")
        return Status.FAILURE