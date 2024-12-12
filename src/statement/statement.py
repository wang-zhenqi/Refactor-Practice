import json
from functools import reduce

from utils import project_root


def usd(number):
    return f"${(number / 100):,.2f}"


def render_plain_text(data):
    result = f"Statement for {data['customer']}\n"

    for perf in data["performances"]:
        result += f" {perf['name']}: {usd(perf['amount'])} ({perf['audience']} seats)\n"

    result += f"Amount owed is {usd(data['total_amount'])}\n"
    result += f"You earned {data['total_volume_credits']} credits\n"
    return result


def render_html(data):
    result = f"<h1>Statement for {data['customer']}</h1>\n"
    result += "<table>\n"
    result += "<tr><th>play</th><th>seats</th><th>cost</th></tr>\n"
    for perf in data["performances"]:
        result += f"<tr><td>{perf['name']}</td><td>{perf['audience']}</td><td>{usd(perf['amount'])}</td></tr>\n"
    result += "</table>\n"
    result += f"<p>Amount owed is <em>{usd(data['total_amount'])}</em></p>\n"
    result += f"<p>You earned <em>{data['total_volume_credits']}</em> credits</p>\n"
    return result


class Statement:
    def __init__(self, _invoices, _plays):
        self.invoices = _invoices
        self.plays = _plays

    @staticmethod
    def amount_for(perf):
        if perf["type"] == "tragedy":
            result = 40000
            if perf["audience"] > 30:
                result += 1000 * (perf["audience"] - 30)
        elif perf["type"] == "comedy":
            result = 30000
            if perf["audience"] > 20:
                result += 10000 + 500 * (perf["audience"] - 20)
            result += 300 * perf["audience"]
        else:
            raise ValueError(f"unknown type: {perf['type']}")
        return result

    @staticmethod
    def total_amount(data):
        return reduce(lambda x, y: x + y["amount"], data["performances"], 0)

    @staticmethod
    def volume_credits_for(perf):
        result = 0
        result += max(perf["audience"] - 30, 0)
        if "comedy" == perf["type"]:
            result += max(perf["audience"] // 5, 0)
        return result

    def total_volume_credits(self, data):
        return reduce(lambda x, y: x + y, map(self.volume_credits_for, data["performances"]), 0)

    def create_statement_data(self):
        result = {
            "customer": self.invoices["customer"],
            "performances": list(map(lambda x: x | self.plays[x["playID"]], self.invoices["performances"])),
        }
        result["performances"] = list(map(lambda x: x | {"amount": Statement.amount_for(x)}, result["performances"]))
        result["total_amount"] = self.total_amount(result)
        result["total_volume_credits"] = self.total_volume_credits(result)
        return result


if __name__ == "__main__":
    invoices = json.load(open(project_root / "resources" / "statement" / "invoices.json"))
    plays = json.load(open(project_root / "resources" / "statement" / "plays.json"))
    statement = Statement(invoices, plays)
    statement_data = statement.create_statement_data()
    print(render_html(statement_data))
    print("===========")
    print(render_plain_text(statement_data))
