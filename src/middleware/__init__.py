from config import appSettings
from fastapi import FastAPI
from middleware.jwt_middleware import JwtMiddleware

from .test_middleware import TestMiddleware
from .token_middleware import TokenMiddleware
from .usetime_middleware import UseTimeMiddleware

# 统一注册中间件方法
# 中间件的执行顺序和注册顺序，正好是相反的；先注册的后执行

# 定义注册顺序
middlewareList = [
    JwtMiddleware,  # jwt
    UseTimeMiddleware,  # 添加耗时请求中间件
    TokenMiddleware,  # 添加token验证中间件
    TestMiddleware,  # 测试中间件
]


# 优化了下注册函数: 先注册的先执行
def registerMiddlewareHandle(app: FastAPI):

    # jwt未开启则不注册
    if appSettings.jwt_enable is False:
        middlewareList.remove(JwtMiddleware)
    # 倒序中间件
    middlewareList.reverse()
    # 遍历注册
    for _middleware in middlewareList:
        app.add_middleware(_middleware)
