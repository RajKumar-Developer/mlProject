from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

# Import or define your ML model function here
# from your_ml_model_module import run_ml_model

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    # Save the file to a temporary location
    with open("temp_file", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run your ML model on the file
    result = run_ml_model("temp_file")  # Implement this function

    # Remove the temporary file after processing
    os.remove("temp_file")

    # Return the result
    return {"result": result}
