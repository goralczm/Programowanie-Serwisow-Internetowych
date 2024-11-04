from dataclasses import dataclass, asdict

@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}