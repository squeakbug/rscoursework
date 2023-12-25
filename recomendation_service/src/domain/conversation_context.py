from uuid import UUID


class ConversationContext:
    """
    Структура контекста разговора
    """

    id: UUID
    queries: list = []
    responses: list = []
