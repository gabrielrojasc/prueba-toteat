from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from fastapi_pagination.ext.tortoise import paginate

from src.database.models import Orders
from src.schemas.orders import OrderSchema


async def get_orders(params):
    return await paginate(Orders, params)


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


async def get_daily_orders():
    orders = await Orders.all().values("date_closed")
    dates = [order["date_closed"].strftime("%Y-%m-%d") for order in orders]
    daily_orders = [
        {"date": date, "count": dates.count(date)} for date in sorted(set(dates))
    ]
    return daily_orders


async def get_monthly_payments():
    orders = (
        await Orders.all().order_by("-date_closed").values("payments", "date_closed")
    )
    monthly_payments = {}
    for order in orders:
        payments = order["payments"]
        amounts = [payment["amount"] for payment in payments]
        month = order["date_closed"].strftime("%Y-%m")
        monthly_payments[month] = monthly_payments.get(month, 0) + sum(amounts)
    monthly_payments = [
        {"date": date, "amount": amount} for date, amount in monthly_payments.items()
    ]
    return monthly_payments


async def get_monthly_total():
    orders = await Orders.all().order_by("-date_closed").values("total", "date_closed")
    monthly_total = {}
    for order in orders:
        total = order["total"]
        month = order["date_closed"].strftime("%Y-%m")
        monthly_total[month] = monthly_total.get(month, 0) + total
    monthly_total = [
        {"date": date, "amount": amount} for date, amount in monthly_total.items()
    ]
    return monthly_total
