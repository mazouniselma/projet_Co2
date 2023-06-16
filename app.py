from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Ajoutez cette ligne pour servir les fichiers statiques (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/page")
def show_page(request: Request):
    message = "Bonjour, c'est une page de démonstration"
    return templates.TemplateResponse("page.html", {"request": request, "message": message})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




