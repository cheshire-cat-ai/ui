from typing import List, Dict

from cat import hook, endpoint
from cat.types import Message
from cat.auth import AuthResource
from cat.routes import create_crud
from cat.routes import CRUDSelect, CRUDUpdate

from ..db import ChatDB


class ChatCreateUpdate(CRUDUpdate):
    messages: List[Message] = []
    context: Dict = {}

class ChatSelect(CRUDSelect):
    messages: List[Message]
    context: Dict

@endpoint.router
def chats_crud():
    router = create_crud(
        db_model=ChatDB,
        prefix="/api/v2/chats",
        tag="Chats",
        auth_resource=AuthResource.CHAT,
        restrict_by_user_id=True,
        search_fields=["name", "messages", "context"],
        select_schema=ChatSelect,
        create_schema=ChatCreateUpdate,
        update_schema=ChatCreateUpdate
    )
    return router


# TODOV2: Piccolo offers `create_pydantic_model`