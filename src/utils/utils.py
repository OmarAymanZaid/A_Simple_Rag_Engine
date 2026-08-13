from fastapi import FastAPI
from langserve import add_routes


def register_langserve_routes(
    app: FastAPI,
    rag_chain,
) -> None:

    add_routes(
        app,
        rag_chain,
        path="/api/rag",
    )