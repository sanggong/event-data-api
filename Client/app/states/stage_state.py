import random

from app.states.state import State


class StageState(State):
    STATE = 'stagein'

    def __init__(self, user):
        self.user = user

    def run(self):
        cleared = random.choice([True, False])
        if cleared:
            self.user.current_state = self.user.clear_state
        else:
            self.user.current_state = self.user.defeat_state

    def get_data(self) -> dict:
        return {'stage': self.user.stage}
