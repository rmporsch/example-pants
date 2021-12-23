from pydantic import BaseModel
from typing import Optional, List


class Move(BaseModel):
    white: str
    black: Optional[str]


class Board(BaseModel):
    fen_string: str
    note: Optional[str]
    moves: List[Move]
