from repositories.posts_repository import PostsRepository
from domains.post import Post
from domains.post_filters import PostFilter


class PostsService:
    repository: PostsRepository

    def __init__(self, repository: PostsRepository) -> None:
        self.repository = repository

    async def get_all_posts(self) -> list[Post]:
        return await self.repository.get_all_posts()

    async def filtered_posts(self, posts: list[Post], filter: PostFilter) -> list[Post]:
        return [post for post in posts if filter.is_post_valid(post)]

    async def get_posts_as_json(self, posts: list[Post]) -> list:
        json_out = []
        for post in posts:
            json_out.append(post.dict())

        return json_out
