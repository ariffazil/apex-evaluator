# A‑PEX API (FastAPI Version)
# Filename: apex_app_api.py
# Description: Serve APEX Score + Humanity Index via REST API

from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI(title="A‑PEX API", description="APEX Dial Evaluator for ArifOS", version="1.0")

# --- Core Logic Functions ---
def apex_score(ak, pr, en, ex):
    return ak * pr * en * ex

def humanity_index(ak, pr, en, ex, k=3):
    x = 0.4 * ak + 0.2 * pr + 0.2 * (en - 1) + 0.2 * ex
    return 1 / (1 + math.exp(-k * x))

def classify_collapse_risk(apex):
    if apex >= 0.5:
        return "✅ Aligned / Legacy-Bearing"
    elif 0.1 <= apex < 0.5:
        return "🟡 Soft Drift / Reversible"
    elif -0.1 < apex < 0.1:
        return "⚪️ Stagnant / No Signal"
    elif -0.5 < apex <= -0.1:
        return "🟠 Hard Drift / Collapse Imminent"
    else:
        return "🔴 Terminal Collapse / Scar Severed"

# --- Request Schema ---
class ApexInput(BaseModel):
    akal: float
    present: float
    energy: float
    exploration: float

# --- API Route ---
@app.post("/evaluate")
def evaluate_apex(data: ApexInput):
    apex = apex_score(data.akal, data.present, data.energy, data.exploration)
    humanity = humanity_index(data.akal, data.present, data.energy, data.exploration)
    risk = classify_collapse_risk(apex)
    return {
        "apex_score": round(apex, 3),
        "humanity_index": round(humanity, 3),
        "collapse_risk": risk
    }
