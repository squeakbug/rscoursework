from uuid import UUID, uuid1


class User:
    """
    Структура пользователя
    """

    id: UUID
    conversation_context_id: UUID
