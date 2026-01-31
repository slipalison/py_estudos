from fastapi import FastAPI

app = FastAPI()

@app.get("/clientes/{id}")
def obter_cliente(id: int):
    return {"id": id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)