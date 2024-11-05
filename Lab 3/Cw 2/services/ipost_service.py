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

    async def edit_random_cached_post(self) -> None:
        pass

    async def edit_post(self, post: Post) -> None:
        pass

    async def save_cache(self, posts: Iterable[Post]) -> None:
        pass

    async def get_cache(self) -> Iterable[Post]:
        pass

    async def clear_cache(self) -> None:
        pass

    async def sort_posts_by_edit_time(self, posts: Iterable[Post]) -> Iterable[Post]:
        pass
