from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Orders
from src.schemas.orders import OrderSchema


async def get_orders():
    return await OrderSchema.from_queryset(Orders.all())


async def get_order(order_id) -> OrderSchema:
    return await OrderSchema.from_queryset_single(Orders.get(id=order_id))


async def create_order(order) -> OrderSchema:
    order_dict = order.dict(exclude_unset=True)
    order_obj = await Orders.create(**order_dict)
    return await OrderSchema.from_tortoise_orm(order_obj)


async def update_order(order_id, order) -> OrderSchema:
    try:
        await OrderSchema.from_queryset_single(Orders.get(id=order_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, deatail=f"Order {order_id} not found")

    await Orders.filter(id=order_id).update(**order.dict(exclude_unset=True))
    return await OrderSchema.from_queryset_single(Orders.get(id=order_id))


async def delete_order(order_id):
    try:
        await OrderSchema.from_queryset_single(Orders.get(id=order_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, deatail=f"Order {order_id} not found")

    deleted_count = await Orders.filter(id=order_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return f"Deleted order {order_id}"
