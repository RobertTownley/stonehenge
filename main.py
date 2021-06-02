from stonehenge import Application, Route, Router, run
from stonehenge.modules import DefaultModules
from stonehenge.admin import AdminRouter
from stonehenge.cms import CMSRouter

from blog import BlogModule
from handlers import home, about, portfolio, subpage, blog_handler, user_handler


class App(Application):
    modules = DefaultModules + [
        BlogModule(),
    ]

    router = Router(
        routes=[
            Route(methods=["GET"], path="/", handler=home),
            Route(methods=["GET"], path="/about", handler=about),
            Route(methods=["GET"], path="/portfolio", handler=portfolio),
            Route(
                methods=["GET"],
                path="/company/:company_id<int>/user/:username<str>/",
                handler=user_handler,
            ),
            Route(methods=["GET"], path="/blog/:slug<slug>/", handler=blog_handler),
            Router(
                path="/pages",
                routes=[
                    Route(methods=["GET"], path="/subpage", handler=subpage),
                ],
            ),
            AdminRouter(path="/secret-hidden-admin"),
            CMSRouter(),
        ],
        request_middlewares=[],
        response_middlewares=[],
    )


app = App()

if __name__ == "__main__":
    run(app)
