from enum import Enum

class EventType(Enum):
    login = 1
    stagein = 2
    clear = 3
    fail = 4
    purchase = 5
