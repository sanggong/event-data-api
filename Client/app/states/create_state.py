from app.states.state import State


class CreateState(State):
    STATE = 'create'

    def __init__(self, user):
        self.user = user

    def run(self):
        self.user.current_state = self.user.login_state

    def get_data(self):
        return None
