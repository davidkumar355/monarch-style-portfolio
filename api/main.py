import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from dotenv import load_dotenv
import sys
import resend
# Ensure Vercel serverless function can find modules in the same api/ directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import init_db, seed_db, get_all_projects

# Force Vercel redeployment to pick up new DATABASE_URL environment variables
# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(application: FastAPI):
    """Initialise and seed the database on server startup."""
    try:
        init_db()
        seed_db()
    except Exception as e:
        print(f"CRITICAL DATABASE INITIALIZATION ERROR: {str(e)}")
    yield


app = FastAPI(
    title="Monarch Intelligence Network API",
    description="Backend API supporting the dossier portfolio, ML projects data, and secure email transmissions.",
    version="2.0.0",
    lifespan=lifespan
)

# Configure CORS to allow the frontend to interact with the API.
# Note: Since the HTML might be opened locally via file:// protocol or via a local server (e.g. localhost:5500),
# we permit all origins, credentials, methods, and headers for development simplicity.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransmissionPayload(BaseModel):
    name: str
    frequency: EmailStr
    transmission_log: str

class Project(BaseModel):
    id: str
    file_number: str
    status: str
    title: str
    description: str
    tech_stack: List[str]
    github_url: Optional[str] = None
    streamlit_url: Optional[str] = None
    bullets: List[str] = []

# ----------------- ENDPOINTS -----------------

@app.get("/")
def read_root():
    """Serves the static index.html frontend directly from FastAPI."""
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(parent_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    
    return {
        "status": "online",
        "system": "Monarch Intelligence Network",
        "access": "granted",
        "documentation": "/docs"
    }

@app.get("/index.html")
def read_index_html():
    """Serves index.html directly from FastAPI."""
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(parent_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    raise HTTPException(status_code=404, detail="index.html not found on this node.")

@app.get("/image_0.png")
def read_image():
    """Serves the agent profile photo directly from FastAPI."""
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(parent_dir, "image_0.png")
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    if os.path.exists("image_0.png"):
        return FileResponse("image_0.png", media_type="image/png")
    raise HTTPException(status_code=404, detail="image_0.png not found on this node.")

@app.get("/logo.png")
def read_logo():
    """Serves the logo directly from FastAPI."""
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logo_path = os.path.join(parent_dir, "logo.png")
    if os.path.exists(logo_path):
        return FileResponse(logo_path, media_type="image/png")
    if os.path.exists("logo.png"):
        return FileResponse("logo.png", media_type="image/png")
    raise HTTPException(status_code=404, detail="logo.png not found on this node.")

@app.get("/favicon.ico")
def read_favicon():
    """Serves the logo as favicon.ico directly from FastAPI."""
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logo_path = os.path.join(parent_dir, "logo.png")
    if os.path.exists(logo_path):
        return FileResponse(logo_path, media_type="image/png")
    if os.path.exists("logo.png"):
        return FileResponse("logo.png", media_type="image/png")
    raise HTTPException(status_code=404, detail="Favicon not found on this node.")



@app.get("/api/projects", response_model=List[Project])
def get_projects():
    """
    Returns the full list of ML projects from the database.
    """
    try:
        return get_all_projects()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database retrieval failed. System Error: {str(e)}"
        )


@app.post("/api/transmit")
def transmit_message(payload: TransmissionPayload):
    """
    Receives contact transmissions and dispatches email notifications.
    """
    if not payload.name or not payload.frequency or not payload.transmission_log:
        raise HTTPException(status_code=400, detail="Missing required field metrics.")
    
    resend_key = os.getenv("RESEND_API_KEY")
    to_email = os.getenv("TO_EMAIL")
    from_email = os.getenv("FROM_EMAIL", "onboarding@resend.dev")
    
    # Simulated transmission if key is missing (for local testing/setup)
    if not resend_key or not to_email:
        print("--- SIMULATED TRANSMISSION (RESEND KEY OR TO_EMAIL MISSING) ---")
        print(f"Sender Name: {payload.name}")
        print(f"Sender Email: {payload.frequency}")
        print(f"Message: {payload.transmission_log}")
        print("----------------------------------------------------------------")
        return {
            "status": "transmitted",
            "frequency_hash": hash(payload.frequency),
            "message": "Simulated secure link established. (Resend API key not configured yet)"
        }
        
    # Real Resend dispatch
    try:
        resend.api_key = resend_key
        params = {
            "from": from_email,
            "to": [to_email],
            "subject": f"[Monarch Network] Secure Briefing from {payload.name}",
            "text": f"Sender Designation: {payload.name}\nSecure Frequency: {payload.frequency}\n\nTransmission Log:\n{payload.transmission_log}"
        }
        r = resend.Emails.send(params)
        print(f"Resend Dispatch response ID: {r.get('id')}")
        return {
            "status": "transmitted",
            "frequency_hash": hash(payload.frequency),
            "message": "Secure link established. Information routed to destination inbox."
        }
    except Exception as e:
        print(f"Resend Dispatch Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to route transmission through secure node.")

if __name__ == "__main__":
    import uvicorn
    # Boot the FastAPI local server on port 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
