from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Employee API")

# Load dataset when app starts
df = pd.read_csv("employees_cleaned.csv")

@app.get("/employees")
def get_employees():
    # Convert DataFrame to dictionary for JSON response
    return df.to_dict(orient="records")
