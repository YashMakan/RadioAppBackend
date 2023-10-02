import uvicorn as uvicorn
from fastapi import FastAPI

from radio_backend import RadioBackend

app = FastAPI()
radio = RadioBackend()


@app.get("/radios")
async def get_radios():
    return radio.get_radios()


if __name__ == "__main__":
    uvicorn.run(app)
