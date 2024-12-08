import pytest

class TestStatement():
    def test_total_amount_should_return_correct_value(self, statement, statement_data):
        result = statement.total_amount(statement_data)
        expected = 173000
        assert result == expected

    def test_total_volume_credit_should_return_correct_value(self, statement, statement_data):
        result = statement.total_volume_credits(statement_data)
        expected = 47
        assert result == expected

    def test_create_statement_data_should_get_correct_data(self, statement, statement_data):
        result = statement.create_statement_data()
        print(result)
        expected = statement_data
        assert result == expected