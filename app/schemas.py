from pydantic import BaseModel
from typing import List

class MatrixRequest(BaseModel):
    matrix: List[List[str]]