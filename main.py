import uvicorn
from fastapi import FastAPI

from predictor import FreshFlowPredictor

predictor = FreshFlowPredictor()

app = FastAPI()


@app.get("/")
async def root():
    return predictor.predict()


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
