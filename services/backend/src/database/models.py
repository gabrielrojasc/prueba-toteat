from tortoise import fields, models


class Orders(models.Model):
    id = fields.CharField(pk=True, max_length=35)
    date_opened = fields.DatetimeField()
    date_closed = fields.DatetimeField()
    total = fields.IntField()
    cashier = fields.CharField(max_length=125)
    waiter = fields.CharField(max_length=125)
    zone = fields.CharField(max_length=63)
    table = fields.IntField()
    diners = fields.SmallIntField()
    products = fields.JSONField()
    payments = fields.JSONField()
