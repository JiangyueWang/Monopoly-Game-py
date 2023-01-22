class Property:
    def __init__(self, name, cost, rent, colour, owner=None):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.colour = colour
        self.owner = owner

    def double_rent(self):
        if self.rent == 2 * self.cost:
            self.rent = self.rent
        else:
            self.rent = 2 * self.rent
