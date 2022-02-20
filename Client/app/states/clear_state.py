from app.states.state import State


class ClearState(State):
    STATE = 'clear'

    def __init__(self, user):
        self.user = user

    def run(self):
        self.user.current_state = self.user.stage_state
        self.user.stage += 1

    def get_data(self) -> dict:
        return {'stage': self.user.stage}
