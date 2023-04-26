from pydantic import BaseModel
from airbyte_api_wrapper.utils import to_camel

class SnakeToCamelBaseModel(BaseModel):
    '''Modelo base que parsea los atributos camelCase del JSON a snake_case de los modelos'''
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True