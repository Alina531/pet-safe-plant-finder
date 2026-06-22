from fastapi import FastAPI

app = FastAPI(title="Pet-Safe Plant Finder", description="Searchable plant database for pet owners", version="0.1.0")

@app.get("/api/health")
def health_check():
    return {"status": "ok"}