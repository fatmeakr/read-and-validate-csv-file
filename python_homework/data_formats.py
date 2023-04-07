import abc
import csv


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

    def read_file(self, file):
        pass


class CSV(DataType):
    @classmethod
    def check_type(cls, file_name: str) -> bool:
        return file_name.lower().endswith('.csv')

    @classmethod
    def get_type(cls, file_name) -> 'XLS':
        if cls.check_type(file_name):
            return CSV()

    def get_dataset(self, csv_reader) -> dict:
        line = 0
        data = []
        for row in csv_reader:
            if line == 0:
                line += 1
            else:
                line += 1
                data.append({
                    "country_name": row["Country"],
                    "priority_code": row["Order Priority"],
                    "region": row["Region"],
                    "total_profit": row["Total Profit"],
                    "total_cost": row["Total Cost"],
                    "order_date": row["Order Date"],
                    "ship_date": row["Ship Date"],
                    "units_sold": row["Units Sold"],
                    "unit_price": row["Unit Price"],
                    "total_revenue": row["Total Revenue"],
                    "unit_cost": row["Unit Cost"],
                })
        return data

    def read_file(self, file):
        return csv.DictReader(file)


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

    def read_file(self, file):
        pass
