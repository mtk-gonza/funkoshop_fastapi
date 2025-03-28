
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import UPLOADS_DIR
from app.routes import auth_route, category_route, product_route, product_specification_route, user_route, licence_route, image_route
from app.database.database import wait_for_db
from app.database.seeds.seerder import run_seeder

app = FastAPI(title='FunkoShop FastAPI', version='1.0.5')

app.mount('/uploads', StaticFiles(directory=UPLOADS_DIR), name='uploads')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth_route.router)
app.include_router(product_route.router)
app.include_router(category_route.router)
app.include_router(licence_route.router)
app.include_router(product_specification_route.router)
app.include_router(image_route.router)
app.include_router(user_route.router)

if __name__ == '__main__': 
    wait_for_db()  
    run_seeder() 
    uvicorn.run(app, host='0.0.0.0', port=4000)
#python main.py; uvicorn main:app --host 0.0.0.0 --port 4000 --reload