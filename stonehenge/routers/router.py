from __future__ import annotations
from typing import List, Union

from .route import Route
from stonehenge.middlewares.middleware import RequestMiddleware, ResponseMiddlware


class Router:
    def __init__(
        self,
        routes: List[Union[Route, Router]],
        request_middlewares: List[RequestMiddleware] = [],
        response_middlewares: List[ResponseMiddlware] = [],
        path: str = "",
    ):
        self.request_middlewares = request_middlewares
        self.response_middlewares = response_middlewares
        self.path = path
        self.routes = routes
