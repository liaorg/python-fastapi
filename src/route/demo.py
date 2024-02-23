from fastapi import APIRouter, Query, Request, HTTPException, Header
from pydantic import BaseModel
from common.response import res_ok

router = APIRouter()


@router.get("/demo")
def test():
    return res_ok(data='test')


# 有类型的路径参数，如  id: int
# 查询参数，可选的可设置为 None，如 q: str | None = None
@router.get("/demo/{id}")
def test_id(id: int, q: str | None = None):
    data = id
    if q:
        data = str(id) + str(q)
    return res_ok(data=data)


# 使用 Pydantic 模型
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# 请求体 + 路径参数 + 查询参数
@router.put("/demo/{item_id}")
async def update_item(
    item_id: int,
    q: str | None = Query(
        default=None, min_length=3, max_length=50, pattern="^fixedquery$"
    ),
    item: Item | None = None,
):
    results = {"item_id": item_id, q: None, item: None}  # type: ignore
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})

    return res_ok(data=results)
