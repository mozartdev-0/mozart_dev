from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Online", "projeto": "Mozart Dev", "mensagem": "API rodando 24h"}

@app.get("/api")
def api_teste():
    return {"data": "Esta é a rota /api que você configurou na Koyeb"}
