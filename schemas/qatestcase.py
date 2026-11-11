
from pydantic import BaseModel, Field


class SchemaQATestcase(BaseModel):

    case_name: str = Field(max_length=100)
    module: str = Field(max_length=100)
    description: str = Field(max_length=300)
