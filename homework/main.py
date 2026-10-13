from contextlib import asynccontextmanager

import database
import urls
from fastapi import FastAPI


# Асинхронный lifespan контекст для инициализации таблиц
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as conn:
        # Асинхронно создаем таблицы в файле базы данных cookbook.db
        await conn.run_sync(database.Base.metadata.create_all)
    yield


app = FastAPI(
    title="API Кулинарной книги (Async)",
    description="Полностью асинхронное API без генераторов yield",
    version="1.0.0",
    lifespan=lifespan,
)

# Подключаем роуты изurls.py
app.include_router(urls.router)


@app.get("/", tags=["Системные"], summary="Проверка статуса сервера")
async def root():
    return {
        "status": "ok",
        "message": "Асинхронное API Кулинарной книги работает успешно",
    }
