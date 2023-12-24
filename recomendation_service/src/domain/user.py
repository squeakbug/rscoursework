from uuid import UUID
from src.rec_system.filter import Filter


class User:
    """
    Структура пользователя
    """

    id: UUID
    conversation_context_id: UUID
    filter: Filter
    likes: list
    dislikes: list
    measure_func_name: str
    strategy_name: str
