from datetime import datetime
from typing import Optional

def to_camel(string: str) -> str:
    '''Convierte un string snake_case a camelCase'''
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])

def convert_timestamp_to_datetime(timestamp: Optional[int]) -> Optional[datetime]:
    return datetime.fromtimestamp(timestamp) if timestamp else None