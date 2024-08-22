from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import lab3

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешите все источники (можете заменить на конкретные, если нужно)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешите все методы (GET, POST, и т.д.)
    allow_headers=["*"],  # Разрешите все заголовки
)

app.include_router(lab3.router)


