from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import requests

PRIVATE_KEY = "f3925f8c-df85-4c08-8827-5ae2bb5a3a51"

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes limitar a los orígenes específicos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str

@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Private-Key": PRIVATE_KEY }
    )
    return response.json()