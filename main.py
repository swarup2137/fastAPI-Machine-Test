from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user, client, project
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(client.router)
app.include_router(project.router)
