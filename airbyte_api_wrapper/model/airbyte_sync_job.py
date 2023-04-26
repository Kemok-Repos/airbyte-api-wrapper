from typing import List
from .base_model import SnakeToCamelBaseModel
from .airbyte_job import Job
from .airbyte_attempt import Attempt

class SyncJobResponse(SnakeToCamelBaseModel):
    job: Job
    attempts: List[Attempt]

    @classmethod
    def from_dict(cls, obj):
        return cls(
            job=Job.parse_obj(obj['job']),
            attempts=[Attempt.from_dict(a) for a in obj['attempts']],
        )