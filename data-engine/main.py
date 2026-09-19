from fastapi import FastAPI

app = FastAPI(
    title="DataForge Data Engine",
    description="Python Data analysis Engine for DataForge",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "data-engine"}
