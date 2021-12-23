import httpx
from cc_schemas.users import User


class UserClient(httpx.AsyncClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def user_configs(self, user: User):
        raise NotImplementedError()
