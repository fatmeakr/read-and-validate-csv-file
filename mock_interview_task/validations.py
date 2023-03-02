import abc
import requests
from typing import Union


class Condition(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def validate(cls, dataset: str):
        raise NotImplementedError


class RegionCondition(Condition):
    @classmethod
    def validate(cls, dataset: str) -> Union[None, str]:
        dataset_country_name = dataset.split(",")[1]
        dataset_region = dataset.split(",")[0]
        url = "https://api.example.com/?countryName={dataset_country_name}"
        api_region = requests.get(url=url).json()['region']
        if api_region != dataset_region:
            return "Region name corresponds to the country name not match."


class PriorityCondition(Condition):
    @classmethod
    def validate(cls, dataset: str) -> Union[None, str]:
        dataset_priority_code = dataset.split(",")[4]
        url = "https://api-priority.example.com/{dataset_priority_code}"
        response = requests.get(url=url).json()
        if response == 0:
            return "Priority code does not exist."


class TotalProfitCondition(Condition):
    MIN_ALLOWD_TOTAL_PROFIT = 1000

    @classmethod
    def validate(cls, dataset: str) -> Union[None, str]:
        try:
            total_profit = int(dataset.split(",")[13])
            if total_profit < cls.MIN_ALLOWD_TOTAL_PROFIT:
                return f"Total profit is less than {cls.MIN_ALLOWD_TOTAL_PROFIT}."
        except ValueError:
            pass


class TotalCostMaxCondition(Condition):
    MAX_ALLOWED_TOTAL_COST = 5000000

    @classmethod
    def validate(cls, dataset: str) -> Union[None, str]:
        try:
            total_cost = int(dataset.split(",")[12])
            if int(total_cost) > cls.MAX_ALLOWED_TOTAL_COST:
                return f"Total cost is bigger than {cls.MAX_ALLOWED_TOTAL_COST}."
        except ValueError:
            pass


class OrderDateCondition(Condition):
    @classmethod
    def validate(cls, dataset: str) -> Union[None, str]:
        try:
            order_date = int(dataset.split(",")[5])
            ship_date = int(dataset.split(",")[7])
            if order_date > ship_date:
                return "Order date is bigger than ship date."
        except ValueError:
            pass


class TotalRevenueCondition(Condition):
    @classmethod
    def validate(cls, dataset: str) -> Union[None, str]:
        try:
            units_sold = int(dataset.split(",")[8])
            unit_price = float(dataset.split(",")[9])
            total_revenue = float(dataset.split(",")[11])
            if units_sold * unit_price != total_revenue:
                return "total revenue not correct."
        except ValueError:
            pass


class TotalCostCondition(Condition):
    @classmethod
    def validate(cls, dataset: str) -> Union[None, str]:
        try:
            units_sold = int(dataset.split(",")[8])
            unit_cost = float(dataset.split(",")[10])
            total_cost = float(dataset.split(",")[12])
            if units_sold * unit_cost != total_cost:
                return "total cost not correct."
        except ValueError:
            pass
