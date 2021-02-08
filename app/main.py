from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz

description ="""

"""

app = FastAPI(
    title='DS API',
    description=description,
    docs_url='/',
)

app.include_router(db.router, tags=['From the Backend'])
app.include_router(ml.router, tags=['Towards the Backend'])
app.include_router(viz.router, tags=['Visualization'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)