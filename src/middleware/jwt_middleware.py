from config import appSettings
from custom_types import JwtData, response
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from utils import JwtManageUtil

# 后期做配置，这里临时演示
# secret_key = "abcd12345@abcdef"

# 不检查
# noCheckTokenPathList = [
#     "/apidoc",
#     "/openapi.json",
#     "/api/user/login"
# ]


class JwtMiddleware(BaseHTTPMiddleware):
    """jwt验证中间件"""

    def __init__(self, app):
        super().__init__(app)
        self.jwtUtil = JwtManageUtil(
            secretKey=appSettings.jwt_secret_key,
            algorithm=appSettings.jwt_algorithm,
            expired=appSettings.jwt_expired,
            iss=appSettings.jwt_iss,
        )

    async def dispatch(self, request: Request, call_next):
        # 判断路由是否需要验证
        path = request.url.path
        # 不检查的路由
        noCheckTokenPathList = appSettings.jwt_no_check_uris.split(",")
        print("不检查的路由:", noCheckTokenPathList)
        if path in noCheckTokenPathList:
            return await call_next(request)
        # 获取token
        token = request.headers.get('x-token', '')
        if token == "":
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response.ResponseFail('token不能为空~')),
            )

        # 验证token
        tokenInfo = self.jwtUtil.decode(token, JwtData)
        if not isinstance(tokenInfo, JwtData):
            # 验证失败
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response.ResponseFail(tokenInfo)),  # type: ignore
            )

        result = await call_next(request)
        print("token解析成功", tokenInfo)
        return result
