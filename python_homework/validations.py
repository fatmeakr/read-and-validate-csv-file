import abc
import requests
from typing import Union


class Condition(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def validate(cls, dataset: str):
        raise NotImplementedError


class RegionCondition(Condition):
    URL = "https://api.example.com/"

    @classmethod
    def validate(cls, row: str) -> Union[None, str]:
        country_name = row["country_name"]
        region = row["region"]
        url = cls.URL + f"?countryName={country_name}"
        api_region = requests.get(url=url).json()['region']
        if api_region != region:
            return "Region name corresponds to the country name not match."


class PriorityCondition(Condition):
    URL = "https://api-priority.example.com/"

    @classmethod
    def validate(cls, row: str) -> Union[None, str]:
        priority_code = row["priority_code"]
        url = cls.URL + f"{priority_code}"
        response = requests.get(url=url).json()
        if response == 0:
            return "Priority code does not exist."


class TotalProfitCondition(Condition):
    MIN_ALLOWD_TOTAL_PROFIT = 1000

    @classmethod
    def validate(cls, row: str) -> Union[None, str]:
        total_profit = row["total_profit"]
        if float(total_profit) < cls.MIN_ALLOWD_TOTAL_PROFIT:
            return f"Total profit is less than {cls.MIN_ALLOWD_TOTAL_PROFIT}."


class TotalCostMaxCondition(Condition):
    MAX_ALLOWED_TOTAL_COST = 5000000

    @classmethod
    def validate(cls, row: str) -> Union[None, str]:
        total_cost = row["total_cost"]
        if float(total_cost) > cls.MAX_ALLOWED_TOTAL_COST:
            return f"Total cost is bigger than {cls.MAX_ALLOWED_TOTAL_COST}."


class OrderDateCondition(Condition):
    @classmethod
    def validate(cls, row: str) -> Union[None, str]:
        order_date = row["order_date"]
        ship_date = row["ship_date"]
        if (order_date) > (ship_date):
            return "Order date is bigger than ship date."


class TotalRevenueCondition(Condition):
    @classmethod
    def validate(cls, row: str) -> Union[None, str]:
        units_sold = row["units_sold"]
        unit_price = row["unit_price"]
        total_revenue = row["total_revenue"]
        if int(units_sold) * float(unit_price) != float(total_revenue):
            return "total revenue not correct."


class TotalCostCondition(Condition):
    @classmethod
    def validate(cls, row: str) -> Union[None, str]:
        units_sold = row["units_sold"]
        unit_cost = row["unit_cost"]
        total_cost = row["total_cost"]
        if int(units_sold) * float(unit_cost) != float(total_cost):
            return "total cost not correct."
