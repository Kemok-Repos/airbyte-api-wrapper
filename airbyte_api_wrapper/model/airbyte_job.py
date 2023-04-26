from datetime import datetime
from .base_model import SnakeToCamelBaseModel

class Job(SnakeToCamelBaseModel):
    id: int
    config_type: str = "sync"
    config_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    