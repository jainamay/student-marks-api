from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load JSON data
with open("q-vercel-python.json", "r") as f:
    students_data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "Please provide at least one name"}

    marks = []
    for student_name in name:
        mark = next(
            (student["marks"] for student in students_data if student["name"].lower() == student_name.lower()), 
            None
        )
        marks.append(mark)

    return {"marks": marks}

@app.get("/")
async def home():
    return {"message": "Use /api?name=X&name=Y to get marks"}
