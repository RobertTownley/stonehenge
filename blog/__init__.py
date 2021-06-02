from stonehenge.modules import Module
from blog.models import BlogPost


class BlogModule(Module):
    models = [
        BlogPost,
    ]
