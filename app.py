from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from functions.login import login
from functions.electricities import electricities
from functions.electricalpers import electrical_performances
from functions.recommendation import recommendations
import sys
sys.path.append('/Envalt_Project/functions')

app = FastAPI()

class Users(BaseModel):
    username: str
    password: str

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {'Hello World!'}
 

@app.post('/login/')
async def loginAPI(user: Users):
    result = login(user.username, user.password) 
    return result


@app.get('/branches/{branchId}/info')
async def getBranch(branchId:str):
    result = electricities(branchId)
    return result


@app.get('/branches/{branchId}/dailyreport')
async def getBranch(branchId:str):
    result = electrical_performances(branchId)
    return result


@app.get('/branches/{branchId}/recommendation')
async def getRecommendation(branchId:str):
    result = recommendations(branchId)
    return result