import json

import pytest

from statement import Statement


@pytest.fixture
def statement():
    invoice = json.load(open("/workspace/Python/resources/invoices.json"))
    plays = json.load(open("/workspace/Python/resources/plays.json"))
    return Statement(invoice, plays)


@pytest.fixture
def statement_data():
    return {
        "customer": "BigCo",
        "performances": [
            {"audience": 55, "name": "Hamlet", "playID": "hamlet", "type": "tragedy", "amount": 65000},
            {"audience": 35, "name": "As You Like It", "playID": "as-like", "type": "comedy", "amount": 58000},
            {"audience": 40, "name": "Othello", "playID": "othello", "type": "tragedy", "amount": 50000},
        ],
        "total_amount": 173000,
        "total_volume_credits": 47,
    }
