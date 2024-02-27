from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from utils import StringUtil


class Additional(BaseModel):
    """额外信息"""

    time: str
    trace_id: str


class HttpResponse(BaseModel):
    """http统一响应"""

    code: int = Field(default=200)  # 响应码
    msg: str = Field(default="处理成功")  # 响应信息
    data: Any = None  # 具体数据
    additional: Additional | None = None  # 额外信息


def ResponseSuccess(resp: Any) -> HttpResponse:
    """成功响应"""
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(
        data=resp,
        additional=Additional(
            time=currentTime,
            trace_id=StringUtil.GenerateMd5(currentTime),
        ),
    )


def ResponseFail(msg: str, code: int = -1) -> HttpResponse:
    """响应失败"""
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(
        code=code,
        msg=msg,
        additional=Additional(
            time=currentTime,
            trace_id=StringUtil.GenerateMd5(currentTime),
        ),
    )
