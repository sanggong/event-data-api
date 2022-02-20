import random

from app.states.state import State
from app.states.purchase_state import PurchaseState


class DefeatState(State):
    STATE = 'fail'

    def __init__(self, user):
        self.user = user

    def run(self):
        purchased = random.choice([True, False])
        if purchased:
            self.user.current_state = self.user.purchase_state
            self.user.purchase_state.price = random.choice([1000, 2000, 3000, 4000, 5000])
            if self.user.currency == 'usd':
                self.user.purchase_state.price //= 1000
            PurchaseState.ID += 1
        else:
            self.user.current_state = self.user.stage_state

    def get_data(self) -> dict:
        return {'stage': self.user.stage}
