from enum import Enum

class ResponseSignal(str, Enum):

    # File Signals
    # =========================================================
    FILE_VALIDATED_SUCCESS = "file_validated_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    FILE_INGEST_SUCCESS = "file_ingest_success"
    FIle_INGEST_FAILED = "file_ingest_failed"


# Model enums
class ModelProvider(str, Enum):
    OPENAI = "OPENAI"
    GOOGLE = "GOOGLE"


class ModelTier(str, Enum):
    FAST = "fast"
    REASONING = "reasoning"

# VectorStore enums
class VectorStoreProvider(str, Enum):
    CHROMA = "CHROMA"
