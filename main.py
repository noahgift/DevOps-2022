from fastapi import FastAPI
import uvicorn
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello O'Reilly DevOps"}

@app.get("/pandas")
async def pandas():
    df = pd.DataFrame(
        [["a", "b"], ["c", "d"]],
        index=["row 1", "row 2"],
        columns=["col 1", "col 2"],
        )
    return df.to_dict() 

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')