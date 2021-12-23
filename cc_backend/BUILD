python_sources()

python_requirements()

pex_binary(
    name = "cc_backend_service",
    dependencies = [
        "cc_backend/requirements.txt:uvicorn",
        "cc_backend/main.py",
    ],
    platforms = [
        "current",
        "macosx-10.9-x86_64-cp-38-cp38",
    ],
    script = "uvicorn",
)
