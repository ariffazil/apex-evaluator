# A-PEX Streamlit App (apex_app.py)
# Interactive Web Interface for APEX Score Evaluation

import streamlit as st
import math

# ---- Core Functions ----
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

# ---- Streamlit UI ----
st.title("🧠 A-PEX: APEX Theory Evaluator")
st.markdown("Use APEX Dial inputs to evaluate alignment, humanity, and collapse risk.")

