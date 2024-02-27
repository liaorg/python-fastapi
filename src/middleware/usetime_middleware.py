import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class UseTimeMiddleware(BaseHTTPMiddleware):
    """计算耗时中间件"""

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        """请求耗时"""
        start_time = time.time()
        # 调用下一个中间件或路由处理函数
        result = await call_next(request)
        process_time = time.time() - start_time
        result.headers["X-Process-Time"] = str(process_time)
        return result
