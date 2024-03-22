import traceback

from custom_types import response
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def appExceptionHandler(request: Request, exc: Exception):
    """自定义全局系统错误"""
    print(traceback.format_exc())
    return JSONResponse(
        content=jsonable_encoder(response.ResponseFail("系统运行异常,稍后重试~")),
        status_code=status.HTTP_200_OK,
    )
