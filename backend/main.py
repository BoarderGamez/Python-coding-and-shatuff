from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock endpoints
@app.get("/api/forecast/hourly")
def get_hourly_forecast():
    return {
        "12AM": {"temp": "50°", "precip": "100%"},
        "Now": {"temp": "-50°"}
    }

@app.get("/api/forecast/weekly")
def get_weekly_forecast():
    return {
        "Monday": {"high": "60°", "low": "40°"},
        "Tuesday": {"high": "55°", "low": "35°"},
        "Wednesday": {"high": "70°", "low": "50°"},
    }

@app.get("/api/finance")
def get_finance_data():
    return {
        "bitcoin": {"value": "$500"},
        "locked": True,
        "brand": "EA SPORTS"
    }

@app.get("/api/scene")
def get_scene_data():
    return {
        "title": "Aircraft Wing",
        "subtitle": "Deth",
        "conditions": {
            "breeze": "Quite Breez",
            "h": "50°",
            "l": "30°"
        },
        "background": "sky_with_wing.jpg",
        "foreground": "person_on_wing.jpg"
    }
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the FastAPI backend!",
        "endpoints": [
            "/api/forecast/hourly",
            "/api/forecast/weekly",
            "/api/finance",
            "/api/scene"
        ]
    }