
from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.connection import client
from routes.auth_router import router as auth_router
from routes.startup_router import router as startup_router

from dependency import get_startup_service
from schedulers.startup_scheduler import StartupScheduler


@asynccontextmanager
async def lifespan(app: FastAPI):

    startup_service = get_startup_service()

    scheduler = StartupScheduler(startup_service)

    scheduler.start()

    yield

    scheduler.shutdown()


app = FastAPI(
    title="Startly AI",
    lifespan=lifespan
)


# Register authentication routes
app.include_router(auth_router)

# Register startup routes
app.include_router(startup_router)


# Home API
@app.get("/")
def home():

    return {
        "message": "Startly AI is running"
    }


# MongoDB connection test
@app.get("/test-db")
def test_database():

    client.admin.command("ping")

    return {
        "message": "MongoDB Atlas connected successfully"
    }


# Print registered routes
print("APP.PY IS LOADED")
print("REGISTERED ROUTES:")

for route in app.routes:

    if hasattr(route, "path"):
        print(route.path)
