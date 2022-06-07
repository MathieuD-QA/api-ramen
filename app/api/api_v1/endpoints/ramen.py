from fastapi import APIRouter, status
from app.schemas import ramens
from app.db import supabases

router = APIRouter()



@router.get("/ramen", status_code=status.HTTP_200_OK)
def reviews_ramen():
    show = supabases.get_show()
    return show

@router.get("/ramen/{id}", status_code=status.HTTP_200_OK)
def review_id(id: int):
    index = supabases.get_index(id)
    return index

@router.post("/ramen", status_code=status.HTTP_201_CREATED)
def created_ramen(payload: ramens.RamenReviewCreate):
    created = supabases.post_created({"Brand":payload.Brand,"Variety":payload.Variety,"Style":payload.Style,"Country":payload.Country,"Stars":payload.Stars,"Review":payload.Review,"Top_Ten":payload.Top_Ten})
    return created

@router.delete("/ramen/{id}", status_code=status.HTTP_200_OK)
def deleted_ramen(id: int):
    deleted = supabases.delete_index(id)
    return deleted