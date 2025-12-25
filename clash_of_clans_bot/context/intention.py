from clash_of_clans_bot.enums.status_enum import Status

class Intention():
    def __init__(self):
        self.intention = None

    def set(self, intention):
        self.intention = intention
        return Status.SUCCESS

    def discard(self):
        self.intention = None
        return Status.SUCCESS
        
    def is_set(self, intention):
        return Status.SUCCESS if intention == self.intention else Status.FAILURE

    def not_set(self):
        return Status.SUCCESS if self.intention is None else Status.FAILURE