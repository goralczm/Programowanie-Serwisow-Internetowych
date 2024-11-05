from abc import ABC
from typing import Iterable
from domains.comment import Comment


class ICommentService(ABC):
    async def get_all_comments(self) -> Iterable[Comment]:
        pass

    async def get_comments_filtered_by_name(self, comments: Iterable[Comment], needle: str) -> Iterable[Comment]:
        pass

    async def get_comments_filtered_by_body(self, comments: Iterable[Comment], needle: str) -> Iterable[Comment]:
        pass

    async def get_comments_as_json(self, comments: Iterable[Comment]) -> list[dict]:
        pass

    async def edit_random_cached_comment(self) -> None:
        pass

    async def edit_comment(self, comment: Comment) -> None:
        pass

    async def save_cache(self, comments: Iterable[Comment]) -> None:
        pass

    async def get_cache(self) -> Iterable[Comment]:
        pass

    async def clear_cache(self) -> None:
        pass

    async def sort_comments_by_edit_time(self, comments: Iterable[Comment]) -> Iterable[Comment]:
        pass
