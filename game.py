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

    def find_winner(self):
        amount_of_cash = self.players[0].cash
        winner_temp = self.players[0]
        print('-----Calculating cash to find winner-----')
        for player in self.players:
            if player.cash > amount_of_cash:
                amount_of_cash = player.cash
                winner_temp = player
        return winner_temp

    def play_game(self):
        self.display_welcome_message_and_game_rules()
        self.create_game_board()
        # game starts
        print(f'-----Game Starts-----')
        print(
            f'current player is {self.players[self.current_player_id].name}')
        round = 0
        while self.is_game_over != True:
            print(f'-----Round {round}-----')
            # current player roll the dice and move on the board
            current_player = self.players[self.current_player_id]
            # curren player move to the position
            current_player.move(self.blocks)
            current_player_position = current_player.position
            current_player_landed_property = self.blocks[current_player_position]
            print(
                f'Player {current_player.name} rolled {current_player.number_of_moves} landed on {current_player_landed_property.name}')
            # once player landed on the property it is not GO
            if current_player_landed_property.name != "GO":
                # if the property doesnt have an owner, player must buy
                if current_player_landed_property.owner is None:
                    print(
                        f'The land does not have an owner yet {current_player.name} must buy it')
                    self.is_game_over = current_player.buy_property(
                        current_player_landed_property)
                    if self.is_game_over:
                        print('game over!')
                        break

                # if the property has an owner, player needs to pay rent to the property owner
                else:
                    if current_player_landed_property.owner is not current_player.name:
                        print(
                            f'property has an owner that is not {current_player.name}')
                        # find the owner of the property
                        for i in range(len(self.players)):
                            if self.players[i].name == current_player_landed_property.owner:
                                landed_property_owner = self.players[i]
                                break
                        # current player pays rent to the property owner
                        self.is_game_over = current_player.pay_rent(
                            current_player_landed_property, landed_property_owner)
                        if self.is_game_over:
                            print('game over!')
                            break
            # once player landed on the property is GO goes to next round
            if self.current_player_id < 3:
                self.current_player_id += 1
            else:
                self.current_player_id = 0
            round += 1

        winner = self.find_winner()
        print(f'winner is {winner.name} has {winner.cash}')
