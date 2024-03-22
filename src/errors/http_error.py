from custom_types import response
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


async def httpExceptionHandler(request, exc: HTTPException) -> JSONResponse:
    """自定义处理HTTPException"""
    print("request:", request)
    print("status_code:", exc.status_code)
    if exc.status_code == status.HTTP_404_NOT_FOUND:
        # 处理404错误
        return JSONResponse(
            content=jsonable_encoder(response.ResponseFail("接口路由不存在~")),
            status_code=status.HTTP_200_OK,
        )
    elif exc.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
        # 处理405错误
        return JSONResponse(
            content=jsonable_encoder(
                response.ResponseFail("请求方式错误，请查看文档确认~")
            ),
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            content=jsonable_encoder(response.ResponseFail(str(exc))),
            status_code=status.HTTP_200_OK,
        )
