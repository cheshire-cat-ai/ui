from typing import List, Dict

from cat import hook
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

@hook
async def after_mad_hatter_refresh(cat):
    router = create_crud(
        db_model=ChatDB,
        prefix="/chats",
        tag="Chats",
        auth_resource=AuthResource.CHAT,
        restrict_by_user_id=True,
        search_fields=["name", "messages", "context"],
        select_schema=ChatSelect,
        create_schema=ChatCreateUpdate,
        update_schema=ChatCreateUpdate
    )

    cat.fastapi_app.include_router(router)

# TODOV2: endpoints are not removed on plugin deactivation
# TODOV2: Piccolo offers `create_pydantic_model`