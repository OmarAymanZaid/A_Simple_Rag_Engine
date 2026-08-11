from enum import Enum

class ResponseSignal(str, Enum):

    # File Signals
    # =========================================================
    FILE_VALIDATED_SUCCESS = "file_validated_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    FILE_INGEST_SUCCESS = "file_ingest_success"
