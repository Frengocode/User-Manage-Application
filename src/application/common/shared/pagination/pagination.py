from pydantic import BaseModel, Field


class BasePagination(BaseModel):
    """Base Pagination"""

    offset: int = Field(min_length=0)
    limit: int = Field(min_length=10)
