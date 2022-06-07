from fastapi import APIRouter, status
from app.schemas import ramens
from app.db import supabases

router = APIRouter()



@router.get("/ramen", status_code=status.HTTP_200_OK)
def get_all_gares():
    show = supabases.get_show()
    return show


