
# TODOV2:
# - rename Context to Project
# - manage relationship with chats externally (middle table)
# - router can be added after bootstrap, or after mad_hatter finishes sync,
#   or one by one via @endpoint
# - how does the frontend know this is supported?

"""
from typing import List

from cat.types import Message
from cat.auth.permissions import AuthResource
from cat.db.models import ContextDB
from ...src.cat.routes.common.crud import create_crud
from ...src.cat.routes.common.schemas import CRUDSelect, CRUDUpdate

from typing import List
from pydantic import BaseModel

from cat.looking_glass import prompts
from cat.protocols.model_context.type_wrappers import Resource
from cat.protocols.model_context.server import MCPServer

class Context(BaseModel):
    instructions: str = prompts.MAIN_PROMPT_PREFIX
    resources: List[Resource] = []
    mcps: List[MCPServer] = []

class ChatSelect(CRUDSelect):
    messages: List[Message]

class ContextCreateUpdate(CRUDUpdate, Context):
    pass

class ContextSelect(CRUDSelect, ContextCreateUpdate):
    chats: List[ChatSelect] = []

router = create_crud(
    db_model=ContextDB,
    prefix="/contexts",
    tag="Contexts",
    auth_resource=AuthResource.CHAT,
    restrict_by_user_id=True,
    search_fields=["name", "system_prompt", "resources"],
    select_schema=ContextSelect,
    create_schema=ContextCreateUpdate,
    update_schema=ContextCreateUpdate
)
"""

