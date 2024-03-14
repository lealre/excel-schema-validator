from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator, ConfigDict
from datetime import datetime
from enum import Enum

class EnumCategory(str, Enum):
    category1 = "category1"
    category2 = "category2"
    category3 = "category3"

class Sales(BaseModel):

    email: EmailStr
    date: datetime
    value: PositiveFloat
    product: str
    amount: PositiveInt
    category: EnumCategory
    
    # Do not allow extra column
    model_config = ConfigDict(extra='forbid')


    @field_validator('category')
    def category_must_be_in_enum(cls, error):
        return error