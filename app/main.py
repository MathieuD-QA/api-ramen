from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.endpoints import ramen
app = FastAPI()
app.include_router(ramen.router)



origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.1.40:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "OK"}
