from fastapi import FastAPI
from core.database.database import Base, engine
from core.users.routers import user_router
from core.memos.routers import memo_router
from core.reply.routers import reply_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_router, prefix="/users",)
app.include_router(memo_router, prefix="/memos",)
app.include_router(reply_router, prefix="/reply",)
