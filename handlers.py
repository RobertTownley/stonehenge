from stonehenge.responses.response import JSONResponse
from stonehenge import Request

from blog.models import BlogPost


async def home(request: Request):
    return JSONResponse({"msg": "This is the home page"})


async def about(request: Request):
    return JSONResponse({"msg": "This is the about page"})


async def portfolio(request: Request):
    return JSONResponse({"msg": "This is a portfolio page"})


async def subpage(request: Request):
    return JSONResponse({"msg": "This is a subpage"})


async def blog_handler(request: Request):
    blog_post = BlogPost.find(slug=request.params["slug"])
    return JSONResponse({"title": str(blog_post.title)})


async def user_handler(request: Request):
    company_id = request.params["company_id"]
    username = request.params["username"]
    msg = f"Hello {username}! Hope you're enjoying Company #{company_id}!"
    return JSONResponse({"msg": msg})
