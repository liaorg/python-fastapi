import errors
import middleware
from common.response import res_bad_request, res_error
from component.ConfigManager import config_manager

# 启动 FastAPI http 服务器
from component.LogManager import log_manager
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from router import RegisterRouterList
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse, PlainTextResponse

logger = log_manager.get_logger("app")

app = FastAPI(redoc_url=None, title="FastAPI学习")
# 全局依赖项
# app = FastAPI(dependencies=[Depends(get_query_token)])
# 路由器的依赖项最先执行，然后是装饰器中的 dependencies，再然后是普通的参数依赖项

# 注册自定义错误处理器
errors.registerCustomErrorHandle(app)

# 注册中间件
middleware.registerMiddlewareHandle(app)

logger.info(f"服务已启动：version: {config_manager.get_value(['version'])}")

# 加载路由
for item in RegisterRouterList:
    app.include_router(item.router, prefix="/api", tags=["demo"])


@app.on_event("startup")
async def startup_event():
    logger.info("服务启动")


@app.get("/")
async def root():
    return f"服务已部署，version：{config_manager.get_value(['version'])}"


# 错误处理部分代码
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    """
    错误处理 HTTP 错误，返回 http 400
    :param request:
    :param exc:
    :return:
    """
    return res_error(code=exc.status_code, msg=exc.detail)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc):
    """
    错误处理，请求无效错误，返回 http 500
    :param request:
    :param exc:
    :return:
    """
    logger.warning(f"收到无效 body：{exc}")
    return res_bad_request(msg="无效body")
