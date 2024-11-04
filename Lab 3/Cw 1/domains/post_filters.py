from dataclasses import dataclass, field
from domains.post import Post

@dataclass
class PostFilter:
    userIds: list[int] = field(default_factory=lambda: [])
    ids: list[int] = field(default_factory=lambda: [])
    title_needles: list[str] = field(default_factory=lambda: [])
    body_needles: list[str] = field(default_factory=lambda: [])


    def is_post_valid(self, post: Post):
        return self._post_userId_contains_userId(post)\
            and self._post_id_contains_id(post) \
            and self._post_title_contains_needle(post) \
            and self._post_body_contains_needle(post)

    def _post_userId_contains_userId(self, post: Post) -> bool:
        foundMatch = False
        for userId in self.userIds:
            if userId == post.userId:
                foundMatch = True

        return foundMatch

    def _post_id_contains_id(self, post: Post) -> bool:
        foundMatch = False
        for id in self.ids:
            if id == post.id:
                foundMatch = True

        return foundMatch

    def _post_title_contains_needle(self, post: Post) -> bool:
        for needle in self.title_needles:
            if needle.lower() not in post.title.lower():
                return False

        return True

    def _post_body_contains_needle(self, post: Post) -> bool:
        for needle in self.body_needles:
            if needle.lower() not in post.body.lower():
                return False

        return True
