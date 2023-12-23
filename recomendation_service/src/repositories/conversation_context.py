from uuid import UUID

from src.domain.conversation_context import ConversationContext


class ConversationContextRepositoryList:
    contexts = []

    def get_context_by_id(self, id: UUID) -> ConversationContext:
        return next((ctx for ctx in self.contexts if ctx.id == id), None)

    def create_context(self, ctx: ConversationContext) -> ConversationContext:
        self.contexts.append(ctx)
        return ctx

    def update_context(self, id: UUID, ctx: ConversationContext) -> ConversationContext:
        pass

    def delete_context(self, id: UUID):
        pass
