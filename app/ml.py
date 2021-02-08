"""Machine learning functions"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Prediction(BaseModel):
    state: str
    zip: int
    fips: int
    crime_rate: float
    rental_rate: float
    walkability_score: float



@router.post('/output')
async def output(reply: Prediction):
    """
    Endpoint used to push all the retrived data to the backend
    """
    return {"rental_rate": "everything we know about this zip code"}

@router.post('/test_output')
async def testing():
    return {'state': 'New York', 'Zip': '10011', 'fips': '49017', 'crime rate': 1.13, 'rental rate': 1500.0, 'walkability_score': 138.4}