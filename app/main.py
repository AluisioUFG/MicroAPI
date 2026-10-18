from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import logging

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.task_routes import router as task_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    logger.info("Application startup")
    yield


app = FastAPI(title="Micro API de Gestão de Tarefas", lifespan=lifespan)
app.include_router(task_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exception: RequestValidationError,
) -> JSONResponse:
    """Return validation errors in a consistent JSON format."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "detail": "Validation failed.",
            "errors": jsonable_encoder(exception.errors()),
        },
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(
    request: Request,
    exception: StarletteHTTPException,
) -> JSONResponse:
    """Return HTTP errors in a consistent JSON format."""
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": jsonable_encoder(exception.detail)},
        headers=exception.headers,
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(
    request: Request,
    exception: Exception,
) -> JSONResponse:
    """Hide unexpected error details and log the failure."""
    logger.exception("Unhandled application error", exc_info=exception)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error."},
    )


@app.get("/health")
def health_check() -> dict[str, str]:
    """Retorna o estado de disponibilidade da API."""
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
