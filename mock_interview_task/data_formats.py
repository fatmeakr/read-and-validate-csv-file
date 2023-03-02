import abc
from typing import BinaryIO


class DataType(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def check_type(cls, file: BinaryIO):
        raise NotImplementedError


class XLS(DataType):
    @classmethod
    def check_type(cls, file: BinaryIO):
        return file.lower().endswith('.xls')


class CSV(DataType):
    @classmethod
    def check_type(cls, file: BinaryIO):
        return file.lower().endswith('.csv')


class XLSX(DataType):
    @classmethod
    def check_type(cls, file: BinaryIO):
        return file.lower().endswith('.xlsx')
