from app.states.state import State


class PurchaseState(State):
    STATE = 'purchase'
    ID = 0

    def __init__(self, user):
        self.user = user
        self.price = 0

    def run(self):
        self.user.current_state = self.user.stage_state

    def get_data(self) -> dict:
        return {'order_id': PurchaseState.ID,
                'currency': self.user.currency,
                'price': self.price
                }
