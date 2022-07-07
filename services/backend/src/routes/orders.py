from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.orders as crud
from src.schemas.token import Status
from src.schemas.orders import OrderSchema

router = APIRouter()


@router.get("/orders", response_model=List[OrderSchema])
async def get_orders():
    return await crud.get_orders()


@router.get("/order/{order_id}", response_model=OrderSchema)
async def get_order(order_id: str) -> OrderSchema:
    try:
        return await crud.get_order(order_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Order does not exist")


@router.post("/orders", response_model=OrderSchema)
async def create_order(order_id: str, order: OrderSchema):
    return await crud.create_order(order)


@router.patch(
    "/order/{order_id}",
    response_model=OrderSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_order(order_id: str, order: OrderSchema):
    return await crud.update_order(order_id, order)


@router.delete(
    "/order/{order_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_order(order_id: str):
    return await crud.delete_order(order_id)
