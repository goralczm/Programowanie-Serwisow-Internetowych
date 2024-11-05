import aiohttp

from typing import Iterable
from datetime import datetime

from domains.post import Post
from repositories.ipost_repository import IPostRepository


class PostRepository(IPostRepository):
    async def get_all_post_params(self) -> Iterable[Post] | None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)

        return parsed_params

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[Post]:
        return [Post(event_time=datetime.now().time(),
                     userId=record.get("userId"),
                     id=record.get("id"),
                     title=record.get("title"),
                     body=record.get("body")) for record in params]
