from piccolo.columns import JSON

from cat.db.models import UserScopedDB

# TODOV2: convert to piccolo syntax (was Tortoise)
#class ContextDB(UserScopedModelDB):
#    system_prompt = fields.TextField()
#    resources = fields.JSONField()
#    mcps = fields.JSONField()
#    class Meta:
#        table = "ccat_projects"

class ChatDB(UserScopedDB):
    messages = JSON()
    context = JSON()

    class Meta:
        tablename = "ccat_chats"

ChatDB.create_table(if_not_exists=True).run_sync()