from typing import Iterable
from datetime import datetime, date
import random

from repositories.icomment_repository import ICommentRepository
from services.icomment_service import ICommentService
from domains.comment import Comment
from utils.consts import MAX_SECONDS_FOR_UNEDITED_RECORD


class CommentService(ICommentService):
    repository: ICommentRepository
    cached_comments: Iterable[Comment]

    def __init__(self, repository: ICommentRepository) -> None:
        self.repository = repository
        self.cached_comments = []

    async def get_all_comments(self) -> Iterable[Comment]:
        return await self.repository.get_all_comments_params()

    async def get_comments_filtered_by_name(self, comments: Iterable[Comment], needle: str) -> Iterable[Comment]:
        return [comment for comment in comments if needle in comment.name]

    async def get_comments_filtered_by_body(self, comments: Iterable[Comment], needle: str) -> Iterable[Comment]:
        return [comment for comment in comments if needle in comment.body]

    async def get_comments_as_json(self, comments: Iterable[Comment]) -> list[dict]:
        return [comment.dict() for comment in comments]

    async def edit_random_cached_comment(self) -> None:
        await self.edit_comment(self.cached_comments[random.randint(0, len(self.cached_comments) - 1)])

    async def edit_comment(self, comment: Comment) -> None:
        comment.event_time = datetime.now().time()

    async def save_cache(self, comments: Iterable[Comment]) -> None:
        self.cached_comments = comments

    async def get_cache(self) -> Iterable[Comment]:
        return self.cached_comments

    async def clear_cache(self) -> None:
        await self.save_cache([comment for comment in self.cached_comments if await self._get_time_diff_in_seconds(comment) < MAX_SECONDS_FOR_UNEDITED_RECORD])

    async def _get_time_diff_in_seconds(self, comment: Comment) -> int:
        time = datetime.now().time()
        timeDiff = datetime.combine(date.today(), time) - datetime.combine(date.today(), comment.event_time)

        return timeDiff.seconds

    async def sort_comments_by_edit_time(self, comments: Iterable[Comment]) -> Iterable[Comment]:
        return sorted(comments, key=lambda x: x.event_time)
