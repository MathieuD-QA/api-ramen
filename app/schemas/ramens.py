from pydantic import BaseModel


class RamenReviewCreate(BaseModel):
    Brand: str
    Variety: str
    Style: str
    Country: str
    Stars: str
    Top_Ten: str
    Review: int




