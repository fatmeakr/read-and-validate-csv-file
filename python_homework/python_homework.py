import os
from typing import BinaryIO
from data_formats import DataType
from validations import Condition

FILENAME = os.path.abspath(os.path.dirname(__file__)) + "/10000_Sales_Records.csv"


class Main:

    @classmethod
    def read_file(cls, file_name: str) -> BinaryIO:
        cls.validate_file_format(file_name)

        file_type = cls.get_file_type(file_name)

        file = open(file_name, "r")
        return (file, file_type)

    @classmethod
    def validate_dataset(cls, dataset: BinaryIO, file_type) -> list[str]:
        issues_list = []
        for row in dataset:
            for subclass in Condition.__subclasses__():
                value = subclass.validate(row, file_type)
                if value and (value not in issues_list):
                    issues_list.append(value)
        return issues_list

    @classmethod
    def validate_file_format(cls, file_name: str) -> None:
        if not cls.get_data_type(file_name):
            raise Exception("File Format is not correct!")

    @staticmethod
    def get_data_type(file_name: str) -> bool:
        checked = []
        for subclass in DataType.__subclasses__():
            checked.append(subclass.check_type(file_name))
        return any(checked)

    @classmethod
    def get_file_type(cls, file_name: str) -> str:
        for subclass in DataType.__subclasses__():
            file_type = subclass.get_type(file_name)
            if file_type:
                return file_type


def main():
    content, file_type = Main.read_file(FILENAME)
    Main.validate_dataset(content, file_type)
    content.close()


if __name__ == "__main__":
    main()
