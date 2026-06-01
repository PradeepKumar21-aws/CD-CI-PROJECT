from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="/code")

# Homepage -> Pradeep Portfolio
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "new.html",
        {"request": request}
    )

# Optional old page
@app.get("/portfolio")
def portfolio(request: Request):
    return templates.TemplateResponse(
        "portfolio.html",
        {"request": request}
    )
