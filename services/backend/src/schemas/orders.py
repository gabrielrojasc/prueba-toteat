from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Orders

OrderSchema = pydantic_model_creator(Orders, name="Orders")
