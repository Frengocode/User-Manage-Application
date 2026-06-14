from pydantic import BaseModel


class BasePagination(BaseModel):
    """Base Pagination"""

    offset: int
    limit: int
