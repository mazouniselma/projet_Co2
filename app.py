from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/form", response_class=HTMLResponse)
async def show_form():
    return """
        <html>
            <head>
                <title>Formulaire</title>
            </head>
            <body>
                <h1>Formulaire</h1>
                <form method="post" action="/submit">
                    <label for="ELECTRICITE">ELECTRICITÉ:</label>
                    <input type="number" id="name" name="name"><br><br>
                    
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email"><br><br>
                    
                    <label for="age">Âge:</label>
                    <input type="number" id="age" name="age"><br><br>
                    
                    <input type="submit" value="Soumettre">
                </form>
            </body>
        </html>
    """

@app.post("/submit")
async def submit_form():
    # Traitement du formulaire
    return {"message": "Formulaire soumis avec succès"}


