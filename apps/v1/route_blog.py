from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.blog import retrieve_all_blogs, retrieve_blog
from db.session import get_db
from typing import Optional


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request, alert: Optional[str]=None, db: Session=Depends(get_db)):
    # print(dir(request))

    blogs = retrieve_all_blogs(db=db)

    return templates.TemplateResponse(
        request=request, 
        name="blogs/home.html",
        context={'blogs': blogs, "alert": alert}
        )



@router.get("/app/blog/{id}/")
def blog_detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    return templates.TemplateResponse(name="blogs/detail.html",
                                      request=request,
                                      context={'blog': blog})





