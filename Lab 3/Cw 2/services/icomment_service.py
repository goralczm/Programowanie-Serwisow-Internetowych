from abc import ABC
from typing import Iterable
from domains.comment import Comment


class ICommentService(ABC):
    async def get_all_comments(self) -> Iterable[Comment]:
        pass

    async def get_comments_filtered_by_title(self, posts: Iterable[Comment], needle: str) -> Iterable[Comment]:
        pass

    async def get_comments_filtered_by_body(self, posts: Iterable[Comment], needle: str) -> Iterable[Comment]:
        pass

    async def get_comments_as_json(self, posts: Iterable[Comment]) -> list[dict]:
        pass