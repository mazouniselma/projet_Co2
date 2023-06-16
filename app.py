from fastapi import FastAPI, Form
from pydantic import BaseModel
from enum import Enum
from typing import Annotated


# Définition de la classe modèle pour le formulaire
class UserForm(BaseModel):
    name: str = Form(...)
    email: str = Form(...)
    fruit: str = Form(...)

# Création de l'application FastAPI
app = FastAPI()

# Route pour la soumission du formulaire
@app.post("/submit")
async def submit_form(user_form: UserForm):
    # Traitement des données du formulaire
    name = user_form.name
    email = user_form.email
    selected_fruit = user_form.fruit
    
    # Exemple d'affichage des données
    return {"message": f"Formulaire soumis avec succès. Nom: {name}, Email: {email}, Fruit sélectionné: {selected_fruit}"}