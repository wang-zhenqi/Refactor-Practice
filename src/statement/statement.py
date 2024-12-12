import json
from functools import reduce


def usd(number):
    return f"${(number / 100):,.2f}"


def renderPlainText(data):
    result = f"Statement for {data['customer']}\n"

    for perf in data["performances"]:
        result += f" {perf['name']}: {usd(perf['amount'])} ({perf['audience']} seats)\n"

    result += f"Amount owed is {usd(data['total_amount'])}\n"
    result += f"You earned {data['total_volume_credits']} credits\n"
    return result


def renderHtml(data):
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
    def __init__(self, invoice, plays):
        self.invoice = invoice
        self.plays = plays

    def amount_for(self, perf):
        result = 0
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

    def total_amount(self, data):
        return reduce(lambda x, y: x + y["amount"], data["performances"], 0)

    def volume_credits_for(self, perf):
        result = 0
        result += max(perf["audience"] - 30, 0)
        if "comedy" == perf["type"]:
            result += max(perf["audience"] // 5, 0)
        return result

    def total_volume_credits(self, data):
        return reduce(lambda x, y: x + y, map(self.volume_credits_for, data["performances"]), 0)

    def create_statement_data(self):
        result = {}
        result["customer"] = self.invoice["customer"]
        result["performances"] = list(map(lambda x: x | self.plays[x["playID"]], self.invoice["performances"]))
        result["performances"] = list(map(lambda x: x | {"amount": self.amount_for(x)}, result["performances"]))
        result["total_amount"] = self.total_amount(result)
        result["total_volume_credits"] = self.total_volume_credits(result)
        return result


if __name__ == "__main__":
    invoice = json.load(open("/workspace/Python/resources/invoices.json"))
    plays = json.load(open("/workspace/Python/resources/plays.json"))
    stmt = Statement(invoice, plays)
    data = stmt.create_statement_data()
    print(renderHtml(data))
