from typing import Optional

from app.states.create_state import CreateState
from app.states.login_state import LoginState
from app.states.stage_state import StageState
from app.states.clear_state import ClearState
from app.states.defeat_state import DefeatState
from app.states.purchase_state import PurchaseState


class User:
    def __init__(self, id, currency, stage=1):
        self.id = id
        self.currency = currency
        self.stage = stage

        self.create_state = CreateState(self)
        self.login_state = LoginState(self)
        self.stage_state = StageState(self)
        self.clear_state = ClearState(self)
        self.defeat_state = DefeatState(self)
        self.purchase_state = PurchaseState(self)

        self.current_state = self.create_state

    def __repr__(self):
        return f"User(id:{self.id}, currency:{self.currency}, stage:{self.stage})"

    def act(self):
        self.current_state.run()

    def get_id(self) -> int:
        return self.id

    def get_state(self) -> str:
        return self.current_state.STATE

    def get_param(self) -> Optional[dict]:
        return self.current_state.get_data()