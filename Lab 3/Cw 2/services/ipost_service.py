from abc import ABC
from typing import Iterable
from domains.post import Post


class IPostService(ABC):
    async def get_all_posts(self) -> Iterable[Post]:
        pass

    async def get_posts_filtered_by_title(self, posts: Iterable[Post], needle: str) -> Iterable[Post]:
        pass

    async def get_posts_filtered_by_body(self, posts: Iterable[Post], needle: str) -> Iterable[Post]:
        pass

    async def get_posts_as_json(self, posts: Iterable[Post]) -> list[dict]:
        pass