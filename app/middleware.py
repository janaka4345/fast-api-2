from fastapi import FastAPI, Request
import time
import logging
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
app = FastAPI()

async def log_request_middleware(request: Request, call_next):
    request_start_time = time.monotonic()
    response = await call_next(request)
    request_duration = time.monotonic() - request_start_time
    log_data = {
        "method": request.method,
        "path": request.url.path,
        "duration": request_duration
    }
    log.info(log_data)
    return response
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(log_request_middleware)