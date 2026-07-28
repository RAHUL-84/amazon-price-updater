from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.scraper import run_scraper
from app.security import verify_token


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/products.xlsx")
async def download_excel():

    return FileResponse(
        "products.xlsx",
        filename="products.xlsx"
    )


@router.get("/dashboard")
async def dashboard(request: Request):

    token = request.cookies.get("token")

    # Token nahi mila
    if not token:
        return RedirectResponse(
            "/",
            status_code=302
        )


    # Token verify karo
    user = verify_token(token)


    # Token invalid ya expire
    if not user:
        return RedirectResponse(
            "/",
            status_code=302
        )


    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "username": user
        }
    )



@router.post("/run")
async def run(request: Request):

    token = request.cookies.get("token")


    # Token nahi mila
    if not token:
        return RedirectResponse(
            "/",
            status_code=302
        )


    # Token verify
    user = verify_token(token)


    # Invalid token
    if not user:
        return RedirectResponse(
            "/",
            status_code=302
        )


    await run_scraper()


    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "username": user,
            "message": "Scraping Completed Successfully."
        }
    )