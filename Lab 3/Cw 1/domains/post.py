from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Post:
    event_time: datetime
    userId: int
    id: int
    title: str
    body: str

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}