from dataclasses import dataclass, asdict

@dataclass
class Post:
    postId: int
    id: int
    name: str
    email: str
    body: str

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}