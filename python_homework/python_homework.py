import os
from typing import BinaryIO
from data_formats import DataType
from validations import Condition

FILENAME = os.path.abspath(os.path.dirname(__file__)) + "/10000_Sales_Records.csv"


def read_file(file_name: str) -> BinaryIO:
    validate_file_format(file_name)
    file_type = get_file_type(file_name)

    with open(file_name, "r") as file:
        content = file_type.read_file(file)
        data = file_type.get_dataset(content)

    return data


def validate_dataset(dataset: BinaryIO) -> list[str]:
    issues_list = []
    for row in dataset:
        for subclass in Condition.__subclasses__():
            value = subclass.validate(row)
            if value and (value not in issues_list):
                issues_list.append(value)
    print(issues_list)
    return issues_list


def validate_file_format(file_name: str) -> None:
    if not get_data_type(file_name):
        raise Exception("File Format is not correct!")


def get_data_type(file_name: str) -> bool:
    checked = []
    for subclass in DataType.__subclasses__():
        checked.append(subclass.check_type(file_name))
    return any(checked)


def get_file_type(file_name: str) -> str:
    for subclass in DataType.__subclasses__():
        file_type = subclass.get_type(file_name)
        if file_type:
            return file_type


def main():
    content = read_file(FILENAME)
    validate_dataset(content)


if __name__ == "__main__":
    main()
