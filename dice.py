import json
import random


class Dice:
    def __init__(self, selected_dice_number):
        self.dice_numbers = []
        with open(f'rolls_{selected_dice_number}.json', 'r') as f:
            dice_data = json.loads(f.read())
            for i in dice_data:
                self.dice_numbers.append(i)

    def generate_rand_num_from_dice(self):
        random_index_of_dice = random.randint(0, len(self.dice_numbers)-1)
        dice_number = self.dice_numbers[random_index_of_dice]
        return dice_number
