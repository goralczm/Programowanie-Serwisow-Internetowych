from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Comment:
    event_time: datetime
    postId: int
    id: int
    name: str
    email: str
    body: str

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}