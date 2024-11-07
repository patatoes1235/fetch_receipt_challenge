from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.router import router

app = FastAPI(
    title="Fetch Reciept Processor Challege Kenneth Zhou",
    debug=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom exception handler for RequestValidationError to return 400 instead of 422 (default)
@app.exception_handler(RequestValidationError)
async def custom_exception_handler(request: Request, exc: RequestValidationError):            
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


app.include_router(router)