from production_plan.producer import Producer


class Province:
    def __init__(self, doc):
        self.name = doc["name"]
        self.producers = []
        self.total_production = 0
        self.demand = doc["demand"]
        self.price = doc["price"]
        for producer in doc["producers"]:
            self.add_producer(Producer(self, producer))

    def add_producer(self, arg):
        self.producers.append(arg)
        self.total_production += arg.production

    def get_name(self):
        return self.name

    def get_producers(self):
        return self.producers

    def get_total_production(self):
        return self.total_production

    def set_total_production(self, arg):
        self.total_production = arg

    def get_demand(self):
        return self.demand

    def set_demand(self, arg):
        self.demand = int(arg)

    def get_price(self):
        return self.price

    def set_price(self, arg):
        self.price = int(arg)

    def shortfall(self):
        return self.demand - self.total_production

    def profit(self):
        return self.demand_value() - self.demand_cost()

    def demand_cost(self):
        result = 0
        remaining_demand = self.demand

        for producer in sorted(self.producers, key=lambda x: x.cost):
            contribution = min(remaining_demand, producer.production)
            remaining_demand -= contribution
            result += producer.cost * contribution
        return result

    def demand_value(self):
        return self.satisfied_demand() * self.price

    def satisfied_demand(self):
        return min(self.demand, self.total_production)
