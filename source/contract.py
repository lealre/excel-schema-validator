from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator, ConfigDict
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"

class Sales(BaseModel):

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: str
    quantidade: PositiveInt
    categoria: CategoriaEnum
    
    # Do not allow extra column
    model_config = ConfigDict(extra='forbid')


    @field_validator('categoria')
    def category_must_be_in_enum(cls, error):
        return error