from dependency_injector.wiring import Provide

import asyncio

from services.post_service import IPostService

from container import Container

async def main(service: IPostService = Provide[Container.service]) -> None:
    all_posts = await service.get_all_posts()

    filtered_posts = await service.get_posts_filtered_by_title(all_posts, 'qui')
    filtered_posts = await service.get_posts_filtered_by_body(filtered_posts, 're')

    print(await service.get_posts_as_json(filtered_posts))

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
