import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from fastapi import FastAPI,Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
from dash_app import app as app_dash
import requests

app = FastAPI()

# Obtenir le chemin absolu vers le repertoire des modeles
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"templates"))

# Obtenir le chemin absolu vers le repertoire statique
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"static"))

# Servir des fichiers statiques
app.mount('/static', StaticFiles(directory=static_dir))

# Configurer le modele Jinja2 pour rendre des fichiers HTML
templates = Jinja2Templates(directory= templates_dir)



user = {"admin":"123"}


# EXTERNAL_API_URL ="http://localhost:8000/info"
EXTERNAL_API_URL ="https://meteoapi-bsabg6c4aaaqc2h9.canadaeast-01.azurewebsites.net/info"

def get_external_info():
    try:
        response = requests.get(EXTERNAL_API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e: 
        print("error de api extern:",e)
        return{
            "date":"N/A",
            "time":"N/A",
            "weather":{
                "city":"N/A",
                "temperature":"N/A",
                "description":"N/A"
            }
        } 
 




@app.get('/')
async def home_page(request:Request):
    information = get_external_info()
    print("information:",information)
    return templates.TemplateResponse("home.html", {"request":request,"info":information })

@app.get('/login')
async def login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request":request})


@app.post('/login')
async def login(request : Request ,username: str = Form(...), password: str = Form(...)):
    if username in user and user[username]==password:
        response = RedirectResponse(url='/dashboard', status_code=302)
        response.set_cookie("Authorization", value="Bearer Token", httponly=True)
        return response
    return templates.TemplateResponse('login.html', {"request":request , "error":"Invalid username and password"})


@app.get('/logout')
async def logout():
    response = RedirectResponse(url='login')
    response.delete_cookie("Authorization")
    return response



# Montez l'application Dash sous le chemin /dashboard

app.mount('/dashboard', WSGIMiddleware(app_dash.server))

