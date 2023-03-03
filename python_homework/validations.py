import abc
import requests
from typing import Union


class Condition(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def validate(cls, dataset: str):
        raise NotImplementedError


class RegionCondition(Condition):
    URL = "https://api.example.com"

    @classmethod
    def validate(cls, dataset: str, file_type) -> Union[None, str]:
        country_name = file_type.get_dataset(dataset)["country_name"]
        region = file_type.get_dataset(dataset)["region"]
        url = cls.URL + f"?countryName={country_name}"
        api_region = requests.get(url=url).json()['region']
        if api_region != region:
            return "Region name corresponds to the country name not match."


class PriorityCondition(Condition):
    URL = "https://api-priority.example.com"

    @classmethod
    def validate(cls, dataset: str, file_type) -> Union[None, str]:
        priority_code = file_type.get_dataset(dataset)["priority_code"]
        url = cls.URL + f"/{priority_code}"
        response = requests.get(url=url).json()
        if response == 0:
            return "Priority code does not exist."


class TotalProfitCondition(Condition):
    MIN_ALLOWD_TOTAL_PROFIT = 1000

    @classmethod
    def validate(cls, dataset: str, file_type) -> Union[None, str]:
        try:
            total_profit = int(file_type.get_dataset(dataset)["total_profit"])
            if total_profit < cls.MIN_ALLOWD_TOTAL_PROFIT:
                return f"Total profit is less than {cls.MIN_ALLOWD_TOTAL_PROFIT}."
        except ValueError:
            pass


class TotalCostMaxCondition(Condition):
    MAX_ALLOWED_TOTAL_COST = 5000000

    @classmethod
    def validate(cls, dataset: str, file_type) -> Union[None, str]:
        try:
            total_cost = int(file_type.get_dataset(dataset)["total_cost"])
            if total_cost > cls.MAX_ALLOWED_TOTAL_COST:
                return f"Total cost is bigger than {cls.MAX_ALLOWED_TOTAL_COST}."
        except ValueError:
            pass


class OrderDateCondition(Condition):
    @classmethod
    def validate(cls, dataset: str, file_type) -> Union[None, str]:
        try:
            order_date = int(file_type.get_dataset(dataset)["order_date"])
            ship_date = int(file_type.get_dataset(dataset)["ship_date"])
            if order_date > ship_date:
                return "Order date is bigger than ship date."
        except ValueError:
            pass


class TotalRevenueCondition(Condition):
    @classmethod
    def validate(cls, dataset: str, file_type) -> Union[None, str]:
        try:
            units_sold = int(file_type.get_dataset(dataset)["units_sold"])
            unit_price = float(file_type.get_dataset(dataset)["unit_price"])
            total_revenue = float(file_type.get_dataset(dataset)["total_revenue"])
            if units_sold * unit_price != total_revenue:
                return "total revenue not correct."
        except ValueError:
            pass


class TotalCostCondition(Condition):
    @classmethod
    def validate(cls, dataset: str, file_type) -> Union[None, str]:
        try:
            units_sold = int(file_type.get_dataset(dataset)["units_sold"])
            unit_cost = float(file_type.get_dataset(dataset)["unit_cost"])
            total_cost = float(file_type.get_dataset(dataset)["total_cost"])
            if units_sold * unit_cost != total_cost:
                return "total cost not correct."
        except ValueError:
            pass
