from typing import Iterable

from dependency_injector.wiring import Provide
import random

import asyncio

from domains.post import Post
from domains.comment import Comment
from services.post_service import IPostService
from services.comment_service import ICommentService
from utils.consts import MAX_SECONDS_FOR_UNEDITED_RECORD

from container import Container

async def simulate_editing_posts(posts_service: IPostService) -> None:
    for i in range(random.randint(1, 5)):
        await posts_service.edit_random_cached_post()

async def simulate_editing_comments(comments_service: ICommentService) -> None:
    for i in range(random.randint(1, 5)):
        await comments_service.edit_random_cached_comment()

async def clear_cache_routine(posts_service: IPostService,
                              comments_service: ICommentService) -> None:
    await posts_service.clear_cache()
    await comments_service.clear_cache()


async def test_clearing_cache(all_posts: Iterable[Post],
                              all_comments: Iterable[Comment],
                              posts_service: IPostService,
                              comments_service: ICommentService) -> None:
    await posts_service.save_cache(all_posts)
    await comments_service.save_cache(all_comments)

    await asyncio.sleep(MAX_SECONDS_FOR_UNEDITED_RECORD + 1)

    await simulate_editing_posts(posts_service)
    await simulate_editing_comments(comments_service)

    await clear_cache_routine(posts_service, comments_service)

    print(await posts_service.get_cache())
    print(await comments_service.get_cache())

async def main(posts_service: IPostService = Provide[Container.posts_service],
               comments_service: ICommentService = Provide[Container.comments_service]) -> None:
    all_posts = await posts_service.get_all_posts()
    all_comments = await comments_service.get_all_comments()

    filtered_posts = await posts_service.get_posts_filtered_by_title(all_posts, 'qui')
    filtered_posts = await posts_service.get_posts_filtered_by_body(filtered_posts, 're')

    filtered_comments = await comments_service.get_comments_filtered_by_name(all_comments, 'expedi')

    print(await posts_service.get_posts_as_json(filtered_posts))
    print(await comments_service.get_comments_as_json(filtered_comments))

    await test_clearing_cache(all_posts,
                              all_comments,
                              posts_service,
                              comments_service)

    sorted_posts = await posts_service.sort_posts_by_edit_time(await posts_service.get_cache())
    sorted_comments = await comments_service.sort_comments_by_edit_time(await comments_service.get_cache())
    print(sorted_posts)
    print(sorted_comments)

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
