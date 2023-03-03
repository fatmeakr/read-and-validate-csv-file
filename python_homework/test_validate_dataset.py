import os
import unittest
from unittest.mock import patch
from python_homework import Main
from validations import RegionCondition, PriorityCondition, TotalProfitCondition, TotalCostMaxCondition


class TestValidateDataset(unittest.TestCase):
    TESTDATA_FILENAME = os.path.abspath(os.path.dirname(__file__)) + "/test_Sales_Records.csv"

    def setUp(self):
        self.content, self.file_type = Main.read_file(self.TESTDATA_FILENAME)

    def tearDown(self):
        self.content.close()

    @patch('validations.requests')
    def test_invalid_region_correspends_to_country(self, mock_requests):
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = "Region name corresponds to the country name not match."

        for row in self.content:
            value = RegionCondition.validate(row, self.file_type)
            if value:
                self.assertEqual(value, "Region name corresponds to the country name not match.")

    @patch('validations.requests')
    def test_invalid_priority_code(self, mock_requests):
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = "Priority code does not exist."

        for row in self.content:
            value = PriorityCondition.validate(row, self.file_type)
            if value:
                self.assertEqual(value, "Priority code does not exist.")

    @patch('validations.requests')
    def test_total_profit_is_less_than_max(self, mock_requests):
        mock_requests.return_value.status_code = 200

        for row in self.content:
            value = TotalProfitCondition.validate(row, self.file_type)
            if value:
                self.assertEqual(value, f"Total profit is less than {TotalProfitCondition.MIN_ALLOWD_TOTAL_PROFIT}.")

    @patch('validations.requests')
    def test_total_cost_is_bigger_than_max(self, mock_requests):
        mock_requests.return_value.status_code = 200

        for row in self.content:
            value = TotalCostMaxCondition.validate(row, self.file_type)
            if value:
                self.assertEqual(value, f"Total cost is bigger than {TotalCostMaxCondition.MAX_ALLOWED_TOTAL_COST}.")


if __name__ == '__main__':
    unittest.main()
