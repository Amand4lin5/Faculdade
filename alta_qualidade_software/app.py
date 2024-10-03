from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request

app = FastAPI()

# Configurar templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Taxas de conversão pré-definidas (exemplo)
exchange_rates = {
    "USD": 1.0,     # Dólar dos EUA
    "EUR": 0.85,    # Euro
    "BRL": 5.25     # Real Brasileiro
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "rates": exchange_rates})

@app.post("/convert/")
async def convert_currency(
    from_currency: str = Form(...),
    to_currency: str = Form(...),
    amount: float = Form(...)
):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return {"error": "Moeda não suportada."}

    # Cálculo da conversão
    converted_amount = (amount / exchange_rates[from_currency]) * exchange_rates[to_currency]
    
    return {"converted_amount": round(converted_amount, 2), "currency": to_currency}
