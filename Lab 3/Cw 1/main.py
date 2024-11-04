import asyncio

from repositories.posts_repository import PostsRepository
from services.posts_service import PostsService
from domains.post_filters import PostFilter


async def main() -> None:
    repository = PostsRepository()
    service = PostsService(repository=repository)

    all_posts = await service.get_all_posts()
    filter = PostFilter(title_needles=['qui'], body_needles=['est', 'rerum'])
    #filter = PostFilter(ids=[1, 2])
    filtered_posts = await service.filtered_posts(all_posts, filter)
    posts_as_json = await service.get_posts_as_json(filtered_posts)

    print(posts_as_json)


if __name__ == "__main__":
    asyncio.run(main())
