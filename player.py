from dice import Dice
import random


class Player:
    def __init__(self, name, cash=16, position=0):
        self.name = name
        self.cash = cash
        self.position = position
        self.properties_owned = []
        self.number_of_moves = 0

    def choose_dice_and_roll(self):
        # ask player to choose which dice to roll
        print('Please select a dice to roll')
        self.player_select_dice = int(
            input('Enter 1 for dice one, enter 2 for dice 2: '))
        self.selected_dice = Dice(self.player_select_dice)

        # randomly pick a number from player chosed cdice
        self.index_of_dice_num = random.randint(
            0, len(self.selected_dice.dice_numbers))
        print(self.selected_dice.dice_numbers)
        return self.selected_dice.dice_numbers[self.index_of_dice_num]

    def move(self):
        self.number_of_moves = self.choose_dice_and_roll()
        self.position += self.number_of_moves
        pass

    def buy_property(self, property):
        pass

    def pay_rent(self, property, amount):
        pass


player = Player('Peter')
print(player.position)
player.move()
print(player.position)
