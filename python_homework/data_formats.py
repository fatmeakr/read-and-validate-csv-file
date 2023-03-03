import abc


class DataType(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def check_type(cls, file_name: str):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def get_type(cls, file_name: str):
        raise NotImplementedError


class XLS(DataType):
    @classmethod
    def check_type(cls, file_name: str) -> bool:
        return file_name.lower().endswith('.xls')

    @classmethod
    def get_type(cls, file_name) -> 'XLS':
        if cls.check_type(file_name):
            return XLS()

    def get_dataset(self, dataset) -> dict:
        pass


class CSV(DataType):
    @classmethod
    def check_type(cls, file_name: str) -> bool:
        return file_name.lower().endswith('.csv')

    @classmethod
    def get_type(cls, file_name) -> 'XLS':
        if cls.check_type(file_name):
            return CSV()

    def get_dataset(self, dataset) -> dict:
        return {
            "country_name": dataset.split(",")[1],
            "priority_code": dataset.split(",")[4],
            "region": dataset.split(",")[0],
            "total_profit": dataset.split(",")[13],
            "total_cost": dataset.split(",")[12],
            "order_date": dataset.split(",")[5],
            "ship_date": dataset.split(",")[7],
            "units_sold": dataset.split(",")[8],
            "unit_price": dataset.split(",")[9],
            "total_revenue": dataset.split(",")[11],
            "unit_cost": dataset.split(",")[10],
        }


class XLSX(DataType):
    @classmethod
    def check_type(cls, file_name: str) -> bool:
        return file_name.lower().endswith('.xlsx')

    @classmethod
    def get_type(cls, file_name) -> 'XLS':
        if cls.check_type(file_name):
            return XLSX()

    def get_dataset(self, dataset) -> dict:
        pass
