from dependency_injector import containers, providers

from repositories.post_repository import PostRepository
from repositories.comment_repository import CommentRepository
from services.post_service import PostService
from services.comment_service import CommentService

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    posts_repository = providers.Singleton(
        PostRepository,
    )

    comments_repository = providers.Singleton(
        CommentRepository,
    )

    posts_service = providers.Factory(
        PostService,
        repository=posts_repository,
    )

    comments_service = providers.Factory(
        CommentService,
        repository=comments_repository
    )
