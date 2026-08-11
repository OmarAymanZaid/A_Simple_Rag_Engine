import os
import aiofiles
from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse

from helpers.config import get_settings, Settings
from controllers import FileController
from enums.enums import ResponseSignal

from loguru import logger

data_router = APIRouter(
    prefix="/api/data",
    tags=["data"],
)

@data_router.post("/upload/")
async def ingest_data(file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
        
    
    # validate the file properties
    file_controller = FileController()

    is_valid, result_signal = file_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )

    file_path, file_id = file_controller.generate_unique_filepath(
        orig_file_name=file.filename
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )

    return JSONResponse(
            content={
                "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id
            }
        )