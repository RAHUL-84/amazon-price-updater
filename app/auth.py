from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.security import create_token


router = APIRouter()


templates = Jinja2Templates(
    directory="app/templates"
)


USERNAME = "admin"
PASSWORD = "admin123"



@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )



@router.post("/login")
async def login(
    request: Request,
    username:str = Form(...),
    password:str = Form(...)
):

    if username == USERNAME and password == PASSWORD:

        token = create_token(username)
        
        print("Generated JWT Token:")
        print(token)


        token = create_token(username)


        response = RedirectResponse(
            "/dashboard",
            status_code=302
        )


        response.set_cookie(
            key="token",
            value=token,
            httponly=True,
            max_age=3600
        )


        return response


    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "error":"Invalid Username or Password"
        }
    )



@router.get("/logout")
async def logout():

    response = RedirectResponse(
        "/",
        status_code=302
    )


    response.delete_cookie(
        "token"
    )


    return response