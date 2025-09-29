# main.py - entry point for the FastAPI application

from fastapi import FastAPI
from routers import pricing, lgi  # Import the API routers

app = FastAPI(title="MISO API Project")

# Include routers for different endpoints
app.include_router(pricing.router, prefix="/pricing", tags=["Pricing"])
app.include_router(lgi.router, prefix="/lgi", tags=["Load/Generation/Interchange"])

# Health check route
@app.get("/")
def root():
    return {"message": "MISO API Project is running"}
