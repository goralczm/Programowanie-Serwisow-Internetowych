from typing import Iterable

from repositories.post_repository import IPostRepository
from services.ipost_service import IPostService
from domains.post import Post

import json

class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def get_all_posts(self) -> Iterable[Post]:
        return await self.repository.get_all_post_params()

    async def get_posts_filtered_by_title(self, posts: Iterable[Post], needle: str) -> Iterable[Post]:
        return [post for post in posts if needle in post.title]

    async def get_posts_filtered_by_body(self, posts: Iterable[Post], needle: str) -> Iterable[Post]:
        return [post for post in posts if needle in post.body]

    async def get_posts_as_json(self, posts: Iterable[Post]) -> list[dict]:
        return [post.dict() for post in posts]
