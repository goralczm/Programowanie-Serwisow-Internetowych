from typing import Iterable
from datetime import datetime, date
import random

from repositories.post_repository import IPostRepository
from services.ipost_service import IPostService
from domains.post import Post
from utils.consts import MAX_SECONDS_FOR_UNEDITED_RECORD

import json

class PostService(IPostService):
    repository: IPostRepository
    cached_posts: Iterable[Post]

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository
        self.cached_posts = []

    async def get_all_posts(self) -> Iterable[Post]:
        return await self.repository.get_all_post_params()

    async def get_posts_filtered_by_title(self, posts: Iterable[Post], needle: str) -> Iterable[Post]:
        return [post for post in posts if needle in post.title]

    async def get_posts_filtered_by_body(self, posts: Iterable[Post], needle: str) -> Iterable[Post]:
        return [post for post in posts if needle in post.body]

    async def get_posts_as_json(self, posts: Iterable[Post]) -> list[dict]:
        return [post.dict() for post in posts]

    async def edit_random_cached_post(self) -> None:
        await self.edit_post(self.cached_posts[random.randint(0, len(self.cached_posts) - 1)])

    async def edit_post(self, post: Post) -> None:
        post.event_time = datetime.now().time()

    async def save_cache(self, posts: Iterable[Post]) -> None:
        self.cached_posts = posts

    async def get_cache(self) -> Iterable[Post]:
        return self.cached_posts

    async def clear_cache(self) -> None:
        await self.save_cache([post for post in self.cached_posts if await self._get_time_diff_in_seconds(post) < MAX_SECONDS_FOR_UNEDITED_RECORD])

    async def _get_time_diff_in_seconds(self, post: Post) -> int:
        time = datetime.now().time()
        timeDiff = datetime.combine(date.today(), time) - datetime.combine(date.today(), post.event_time)

        return timeDiff.seconds

    async def sort_posts_by_edit_time(self, posts: Iterable[Post]) -> Iterable[Post]:
        return sorted(posts, key=lambda x: x.event_time)
