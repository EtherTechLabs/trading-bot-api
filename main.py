from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from routers.ativo import router


app = FastAPI()

app.include_router(router)



