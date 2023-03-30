from fastapi import File,FastAPI
app = FastAPI()

@app.post("/objectdetection/")
async def get_body(file: bytes = File(...)):
  return {"result": "ok"}