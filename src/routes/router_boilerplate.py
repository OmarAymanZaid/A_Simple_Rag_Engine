from fastapi import FastAPI, APIRouter, Depends,status, Request
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings


router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)
