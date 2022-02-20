from app.states.state import State


class LoginState(State):
    STATE = 'login'

    def __init__(self, user):
        self.user = user

    def run(self):
        self.user.current_state = self.user.stage_state

    def get_data(self):
        return None
