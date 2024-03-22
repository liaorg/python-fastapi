from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .app_error import appExceptionHandler
from .http_error import httpExceptionHandler
from .validation_error import validationExceptionHandler


def registerCustomErrorHandle(server: FastAPI):
    """统一注册自定义错误处理器"""
    # 注册参数验证错误,并覆盖模式RequestValidationError
    server.add_exception_handler(RequestValidationError, validationExceptionHandler)  # type: ignore
    # 错误处理StarletteHTTPException
    server.add_exception_handler(StarletteHTTPException, httpExceptionHandler)  # type: ignore
    # 自定义全局系统错误
    server.add_exception_handler(Exception, appExceptionHandler)
