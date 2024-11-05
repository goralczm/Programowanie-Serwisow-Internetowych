import aiohttp

from typing import Iterable
from datetime import datetime

from domains.comment import Comment
from repositories.icomment_repository import ICommentRepository


class CommentRepository(ICommentRepository):
    async def get_all_comments_params(self) -> Iterable[Comment] | None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)

        return parsed_params

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://jsonplaceholder.typicode.com/comments') as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[Comment]:
        return [Comment(event_time=datetime.now().time(),
                        postId=record.get("postId"),
                        id=record.get("id"),
                        name=record.get("name"),
                        email=record.get("email"),
                        body=record.get("body")) for record in params]
