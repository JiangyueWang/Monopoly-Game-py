import json
import time
from property import Property
from player import Player


class Game:
    def __init__(self):
        self.players = []
        self.blocks = []
        self.properties = []
        self.current_player_id = 0
        self.is_game_over = False

    def display_welcome_message_and_game_rules(self):
        # display welcome message
        # display game rules
        pass

    def add_blocks(self):
        # add blockes and properties on to the game board
        with open('board.json', 'r') as f:
            board_data = f.read()
            block_data = json.loads(board_data)

        for block in block_data:
            if block['name'] == "GO":
                property_name = block['name']
                self.blocks.append(
                    Property(property_name, 0, 0, None))

            else:
                property_name = block['name']
                property_cost = block['price']
                property_rent = property_cost
                property_colour = block['colour']
                self.blocks.append(
                    Property(property_name, property_cost, property_rent, property_colour))
                self.properties.append(
                    Property(property_name, property_cost, property_rent, property_colour))

    def add_players(self):
        # add players to the board
        self.players = [Player('Peter'), Player(
            'Billy'), Player('Charlotte'), Player('Sweedal')]

    def create_game_board(self):
        # create game board with block and players information displayed
        print('-----Generating the game board-----')
        self.add_blocks()
        # time.sleep(2)
        for i in range(len(self.blocks)):
            print(f'Block Name: {self.blocks[i].name}\nBlock Position: {i}')
            print('----------')
            # time.sleep(1)
        print('-----Adding players to the game-----')
        self.add_players()
        # time.sleep(2)
        for i in range(len(self.players)):
            print(
                f'Player {i+1}: {self.players[i].name}\nCash ${self.players[i].cash}\nPosition: {self.players[i].position}')
            print('----------')
            # time.sleep(1)

    def play_game(self):
        self.display_welcome_message_and_game_rules()
        self.create_game_board()
        # game starts
        print(f'-----Game Starts-----')
        print(
            f'current player is {self.players[self.current_player_id].name}')
        round = 0
        while self.is_game_over != True:
            # current player roll the dice and move on the board
            current_player = self.players[self.current_player_id]
            print(f'-----Round {round}-----')

            current_player.move(self.blocks)
            current_player_position = current_player.position
            current_player_landed_property = self.blocks[current_player_position]
            print(
                f'Player {current_player.name} rolled {current_player.number_of_moves} landed on {current_player_landed_property.name}')
            print(
                f'owner of the land is {current_player_landed_property.owner}')
            # once player landed on the property it is not GO
            if current_player_landed_property.name != "GO":
                # if the property doesnt have an owner, player must buy
                if current_player_landed_property.owner is None:
                    self.is_game_over = current_player.buy_property(
                        current_player_landed_property)
                    if self.is_game_over:
                        break
                    else:
                        for i in range(len(current_player.properties_owned)):
                            print(
                                f'{current_player.name} now owns property {current_player.properties_owned[i].name}')
                else:
                    # if the property has an owner, player needs to pay rent to the property owner
                    print(f'property has an owner')
                    if current_player_landed_property.owner is not current_player.name:
                        current_player.pay_rent()

            # once player landed on the property is GO goes to next round
            if self.current_player_id < 3:
                self.current_player_id += 1
            else:
                self.current_player_id = 0
            round += 1
