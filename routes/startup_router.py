
from fastapi import APIRouter, Depends, HTTPException

from services.startup_service import StartupService
from dependency import get_startup_service


router = APIRouter(
    prefix="/startups",
    tags=["Startups"]
)


@router.get("/with-contacts")
def get_startups_with_contacts(
    startup_service: StartupService = Depends(get_startup_service)
):

    try:
        startups = startup_service.get_startups_with_contacts()

        return {
            "total": len(startups),
            "startups": startups
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
