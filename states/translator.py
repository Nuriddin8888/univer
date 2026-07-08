from aiogram.fsm.state import State, StatesGroup


class TranslatorState(StatesGroup):
    text = State()