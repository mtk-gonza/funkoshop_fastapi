
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.views import auth_view, category_view, product_view, product_specification_view, user_view
from src.models.database import wait_for_db
from src.config.seeds.seerder import load_seed_data

app = FastAPI(title='FunkoShop FastAPI', version='1.0.0')

app.mount('/uploads', StaticFiles(directory='uploads'), name='uploads')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth_view.router)
app.include_router(product_view.router)
app.include_router(category_view.router)
app.include_router(product_specification_view.router)
app.include_router(user_view.router)

if __name__ == '__main__': 
    wait_for_db()  
    load_seed_data() 
    uvicorn.run(app, host='0.0.0.0', port=4000)
#python main.py; uvicorn main:app --host 0.0.0.0 --port 4000 --reload