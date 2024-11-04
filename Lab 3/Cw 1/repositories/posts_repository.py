import aiohttp

from typing import Iterable

from utils import consts
from domains.post import Post


class PostsRepository:
    async def get_last_post_params(self) -> Iterable[Post] | None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)

        if len(parsed_params) == 0:
            return None

        return parsed_params[0]

    async def get_all_posts(self) -> Iterable[Post] | None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)

        return parsed_params

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_URL) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[Post]:
        return [Post(event_time=record.get("date"),
                     userId=record.get("userId"),
                     id=record.get("id"),
                     title=record.get("title"),
                     body=record.get("body")) for record in params]
