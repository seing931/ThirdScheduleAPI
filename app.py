from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Input model
class ContributionRequest(BaseModel):
    wages: float
    nationality: str
    age: int

# Function to calculate employer/employee share
def calculate_contribution(wages: float, nationality: str, age: int):
    # Example: Simple logic (replace with actual Third Schedule logic)
    if nationality.lower() == "malaysian":
        employer_share = wages * 0.13
        employee_share = wages * 0.11
        section_type = "Part A"
    else:
        employer_share = wages * 0.12
        employee_share = wages * 0.10
        section_type = "Part B"
    
    return {
        "employer_share": round(employer_share, 2),
        "employee_share": round(employee_share, 2),
        "section_type": section_type
    }

# FastAPI route
@app.post("/calculate")
async def calculate(request: ContributionRequest):
    return calculate_contribution(request.wages, request.nationality, request.age)
