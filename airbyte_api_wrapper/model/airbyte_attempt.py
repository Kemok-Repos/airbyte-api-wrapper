from datetime import datetime
from typing import Optional
from pydantic import validator
from utils import convert_timestamp_to_datetime
from .base_model import SnakeToCamelBaseModel
from .airbyte_log import Log

class Attempt(SnakeToCamelBaseModel):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    ended_at: Optional[datetime]
    bytes_synced: Optional[int]
    records_synced: Optional[int]
    records_emitted: Optional[int]
    bytes_emitted: Optional[int]
    state_messages_emitted: Optional[int]
    records_committed: Optional[int]
    logs: Optional[Log]

    @classmethod
    def from_dict(cls, obj):
        '''Parsea el dict response de Airbyte al modelo correspondiente'''
        return cls(
            id=obj['attempt']['id'],
            status=obj['attempt']['status'],
            created_at=obj['attempt'].get('createdAt', None),
            updated_at=obj['attempt'].get('updatedAt', None),
            ended_at=obj['attempt'].get('endedAt', None),
            bytes_synced=obj['attempt'].get('bytesSynced', None),
            records_synced=obj['attempt'].get('recordsSynced', None),
            records_emitted=obj['attempt'].get('totalStats', {}).get('recordsEmitted', None),
            bytes_emitted=obj['attempt'].get('totalStats', {}).get('bytesEmitted', None),
            state_messages_emitted=obj['attempt'].get('totalStats', {}).get('stateMessagesEmitted', None),
            records_committed=obj['attempt'].get('totalStats', {}).get('recordsCommitted', None),
            logs=Log.parse_obj(obj.get('logs', None)),
        )
    
    @validator('created_at', 'updated_at', 'ended_at', pre=True)
    def convert_timestamps(cls, v):
        '''Valida la conversión de timestamps a fechas o retorna None cuando no existan'''
        return convert_timestamp_to_datetime(v)