from typing import BinaryIO, Generator
from data_formats import DataType
from validations import Condition


class Main:
    @classmethod
    def get_data_type(self, file_name: str) -> bool:
        checked = []
        for subclass in DataType.__subclasses__():
            checked.append(subclass.check_type(file_name))
        return any(checked)

    @classmethod
    def validate_file_format(cls, file_name: str) -> None:
        if not cls.get_data_type(file_name):
            raise Exception("File Format is not correct!")

    @classmethod
    def read_file(cls, file_name: str) -> BinaryIO:
        cls.validate_file_format(file_name)

        file = open(file_name, "r")
        return file

    @classmethod
    def validate_dataset(cls, dataset: BinaryIO) -> list[str]:
        issues_list = []
        for row in dataset:
            for subclass in Condition.__subclasses__():
                value = subclass.validate(row)
                if value and (value not in issues_list):
                    issues_list.append(value)
        return issues_list


def main():
    file = Main.read_file('10000_Sales_Records.csv')
    Main.validate_dataset(file)


if __name__ == "__main__":
    main()
