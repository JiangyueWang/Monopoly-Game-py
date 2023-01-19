from dice import Dice


class Player:
    def __init__(self, name, cash=16, position=0):
        self.name = name
        self.cash = cash
        self.position = position
        self.properties_owned = []
        self.number_of_moves = 0

    def roll(self):
        # generate random numbers from dice one and two
        rand_num_from_dice_one = Dice(1).generate_rand_num_from_dice()
        rand_num_from_dice_two = Dice(2).generate_rand_num_from_dice()
        return rand_num_from_dice_one+rand_num_from_dice_two

    def move(self, blocks):
        # self.number_of_moves = self.roll()
        self.number_of_moves = 15
        self.position += self.number_of_moves
        if self.position >= len(blocks):
            self.position -= len(blocks)
            self.cash += 1
            print(f'{self.name} passed GO and received $1')

    def buy_property(self, landed_property):
        pass

    def pay_rent(self, property, amount):
        pass


# player1 = Player('Peter')
# player1.move()
# print(player1.number_of_moves)
