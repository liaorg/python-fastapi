from config import keyErrorChineseDict, validateChineseDict
from custom_types import response
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validationExceptionHandler(request: Request, exc: RequestValidationError):
    """自定义参数验证异常错误"""
    errMsg = ""
    for error in exc.errors():
        fieldName = ".".join(error.get("loc"))
        errType = error.get("type")
        if errType in validateChineseDict:
            # 在定义错误模版中，并翻译出内容
            translateMsg = translate(fieldName, errType, error.get("ctx")) + "; "
            if translateMsg:
                errMsg += translateMsg
        else:
            # 不在定义模型，显示原始错误
            errMsg += ".".join(error.get("loc")) + "[" + error.get("type") + "]:" + error.get("msg") + "; "

    # 替换body.
    errMsg = errMsg.replace("body.", "")
    # 返回
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(response.ResponseFail(errMsg)),
    )


def translate(fieldName: str, errType: str, limitDict: dict) -> str:
    """翻译错误信息"""
    # 先判断是否满足关键词错误
    for k, v in keyErrorChineseDict.items():
        if fieldName.find(k) != -1:
            return v

    limitValList = limitDict.values()
    try:
        return validateChineseDict.get(errType).format(fieldName, *limitValList)  # type: ignore
    except Exception:
        return ""
