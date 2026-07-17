from aiogram.fsm.state import State, StatesGroup


class TranslateState(StatesGroup):
    text = State()
    language = State()