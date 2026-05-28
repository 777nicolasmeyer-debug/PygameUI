class States:
    def __init__(self, state):
        self.current = None
        self.state = state

    def set_state(self, state):
        self.current = state
        return state
