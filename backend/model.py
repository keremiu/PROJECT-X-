from pydantic import BaseModel
from typing import Optional, List

class Query(BaseModel):
    name: Optional[str] = None
    tags: Optional[List[str]] = None
    category: Optional[List[str]] = None
    period: Optional[str] = None
    ordering: Optional[str] = None