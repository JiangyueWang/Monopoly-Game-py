class Player:
    def __init__(self, name, cash=16, position=0):
        self.name = name
        self.cash = cash
        self.position = position
        self.properties_owned = []

    def choose_dice_and_roll(self):
        pass

    def move(self, spaces):
        pass

    def buy_property(self, property):
        pass

    def pay_rent(self, property, amount):
        pass
