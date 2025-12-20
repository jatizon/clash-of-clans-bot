


class IfThenElse:
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def execute(self):
        if self.condition():
            return self.then_branch.tick()
        else:
            return self.else_branch.tick()