from abc import ABC
from typing import Iterable
from repositories.icomment_repository import ICommentRepository
from services.icomment_service import ICommentService
from domains.comment import Comment


class CommentService(ICommentService):
    repository: ICommentRepository
    async def get_comments_filtered_by_title(self, needle: str) -> Iterable[Comment]:
        pass

    async def get_comments_filtered_by_body(self, needle: str) -> Iterable[Comment]:
        pass

    async def get_comments_as_json(self, posts: Iterable[Comment]) -> dict:
        pass
