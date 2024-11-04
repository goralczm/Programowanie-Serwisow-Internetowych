from abc import ABC
from typing import Iterable

from domains.comment import Comment


class ICommentRepository(ABC):
    async def get_all_comment_params(self) -> Iterable[Comment] | None:
        pass
