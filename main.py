from fastapi import FastAPI
from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()

# Define a schema for the input data
class SumRequest(BaseModel):
    number1: float
    number2: float

# Define a schema for the output data
class SumResponse(BaseModel):
    result: float

# Root endpoint for welcome message
@app.get("/")
async def root():
    return {"message": "Welcome to the Calculate Sum API!"}

# POST endpoint for calculating the sum
@app.post("/calculate_sum", response_model=SumResponse)
async def calculate_sum(request: SumRequest):
    result = request.number1 + request.number2
    return {"result": result}
