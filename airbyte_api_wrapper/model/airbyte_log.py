from typing import List
from .base_model import SnakeToCamelBaseModel

class Log(SnakeToCamelBaseModel):
    log_lines: List[str]