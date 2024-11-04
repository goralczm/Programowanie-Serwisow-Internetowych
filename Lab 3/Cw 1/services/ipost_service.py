from abc import ABC
from typing import Iterable
from domains.post import Post


class IPostService(ABC):
    async def get_posts_filtered_by_title(self, needle: str) -> Iterable[Post]:
        pass

    async def get_posts_filtered_by_body(self, needle: str) -> Iterable[Post]:
        pass

    async def get_posts_as_json(self, posts: Iterable[Post]) -> dict:
        pass
