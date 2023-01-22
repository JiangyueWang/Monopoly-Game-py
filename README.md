# Monopoly-Game-py

## Woven Monopoly Game
**Objective of ths application**

This application is designed to play the game of Woven Monopoly amoung four players in the terminal

## Language Used 
Python


## Algorithm for the Game

1. Display welcome message
2. Display game rules
3. Create game board, display game board with Go block and all properties, each property on the board has name, cost, rent, owner instance variables
5. Create players, display player information, each player has a name, cash(starting cash is $16), position(starting position is 0), properties_own(starting with an empty list)
6. There are four players who take turns in the following order:
  - Peter
  - Billy
  - Charlotte
  - Sweedal
7. Game starts
8. Player one rolls two dice, the number of moves will become the sum of randomly generated number from two dice
9. Player one moves to the position
10. Display the position player_one has landed
11. Check if player_one lands on a property or not, if player_one lands on GO, player_one's cash increased by $1, if player_one lands on a property, check whether the property has an owner, if no owner, player_one must buy it, if there is an owner of the property, player_one's cash needs to deduct the rent, owner of the property's cash increase by amount of rent
12. check if player_one has enough cash, not enough cash, find who has the highest cash on hand, if player_one has enough cash, check owns colour of the property
13. Move to the next player till the one of the player goes bankrupt
