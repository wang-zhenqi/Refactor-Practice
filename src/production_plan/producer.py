class Producer:
    def __init__(self, a_province, data):
        self.province = a_province
        self.cost = data["cost"]
        self.name = data["name"]
        self.production = data["production"] or 0

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def set_cost(self, arg):
        self.cost = int(arg)

    def get_production(self):
        return self.production

    def set_production(self, amount_str):
        amount = int(amount_str)
        new_production = amount if amount else 0
        self.province.set_total_production(self.province.get_total_production() - self.production + new_production)
        self.production = new_production
