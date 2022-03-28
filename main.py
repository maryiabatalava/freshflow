import uvicorn
from fastapi import FastAPI

from algo import FreshFlowOutput

processor = FreshFlowOutput()

app = FastAPI()


@app.get("/")
async def root():
    return processor.get_output()


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
