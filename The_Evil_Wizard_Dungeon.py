"""
The Evil Wizard Dungeon: TextBasedGame.py

The TextBasedGame.py is a text based game.
The goal is to collect all the 7 items from each room,
before encountering the Evil Wizard in the Throne Room.

The player is required to:
Move between rooms. inpout(North, South, East, West) or 'Exit' to end the game
Collect Items. input(Yes/No)

Note: Every function in this program includes a docstring.

Author: Filip Clefos
Creation date: 14/06/2023
Revisions: Filip Clefos (18/06/2023): changed the While Loop condition in main() Function
"""


# Function to print the Rules and Goal of the game
def show_story_instructions(current_location, items):
    """
    Function runs once and should not be inside the main WHILE LOOP.
    The text it prints includes a brief description of the game and rules to follow.
    The player will also be shown the room they are in and the list of items they have(NONE).

    :param current_location: str, player starting room location
    :param items: list, player inventory items which should be empty.
    :return: None
    """
    print("""
     #######                   #######                       #     #                                     ######                                            
        #    #    # ######     #       #    # # #            #  #  # # ######   ##   #####  #####        #     # #    # #    #  ####  ######  ####  #    # 
        #    #    # #          #       #    # # #            #  #  # #     #   #  #  #    # #    #       #     # #    # ##   # #    # #      #    # ##   # 
        #    ###### #####      #####   #    # # #            #  #  # #    #   #    # #    # #    #       #     # #    # # #  # #      #####  #    # # #  # 
        #    #    # #          #       #    # # #            #  #  # #   #    ###### #####  #    #       #     # #    # #  # # #  ### #      #    # #  # # 
        #    #    # #          #        #  #  # #            #  #  # #  #     #    # #   #  #    #       #     # #    # #   ## #    # #      #    # #   ## 
        #    #    # ######     #######   ##   # ######        ## ##  # ###### #    # #    # #####        ######   ####  #    #  ####  ######  ####  #    #                            
    """)

    print('\nYou find yourself inside a dungeon and before you is a message on the wall')
    print('\nThe only way out of this dungeon is to defeat the Evil with the key that is in The Throne Room.'
          '\nYou first must uncover the dungeon secrets and collect all 7 items that will help you '
          'defeat the Evil Wizard. \nThe items are: \nthe amethyst belt in the Amethyst Shrine, \nthe diamond body '
          'armor in '
          'the Diamond Library, \nthe ruby boots in the Ruby Depository, \nthe sapphire helm in the Sapphire Foyer, '
          '\nthe emerald shield in the Emerald Laboratory, \nthe rubellite amulet in the Rubellite Observatory, '
          '\nthe magic sword in the Music Hall. \nAfter you have gathered all of these items, proceed directly to the '
          'Throne Room where you will find the Evil Wizard.')

    # Print in morse code 'The Evil Wizard Dungeon'
    print('\n- .... .   . ...- .. .-..    .-- .. --.. .- .-. -..    -.. ..- -. --. . --- -. ')

    print('\nTo move between rooms type: North, West, South, East\n')
    print('But move carefully if you enter the Evil Wizard\'s room without first collecting all the items you will be '
          'trapped in the dungeon forever')

    # Print player location
    print('\nYou are now in the {location} You can go from here South or East'.format(location=current_location))
    # Print Inventory items
    print('Inventory Item: {items}'.format(items=items))


# Function prints GAME OVER
def game_over():
    """
    Function prints an ASCII drawing of 'GAME OVER'
    :return:None
    """
    print("""
        .----------------.  .----------------.  .----------------.  .----------------.               .----------------.  .----------------.  .----------------.  .----------------. 
        | .--------------. || .--------------. || .--------------. || .--------------. |             | .--------------. || .--------------. || .--------------. || .--------------. |
        | |    ______    | || |      __      | || | ____    ____ | || |  _________   | |             | |     ____     | || | ____   ____  | || |  _________   | || |  _______     | |
        | |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |             | |   .'    `.   | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |
        | | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |             | |  /  .--.  \  | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |
        | | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |             | |  | |    | |  | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |
        | | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |             | |  \  `--'  /  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |
        | |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |             | |   `.____.'   | || |     \_/      | || | |_________|  | || | |____| |___| | |
        | |              | || |              | || |              | || |              | |             | |              | || |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' || '--------------' |             | '--------------' || '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'  '----------------'  '----------------'               '----------------'  '----------------'  '----------------'  '----------------' 
            """)


# Function for the text to print when the player loses the game
def defeated_text():
    """
    Function will print the text in case the player encounters the Evil Wizard before collecting the 7 required items.
    :return: None
    """
    print('You see the Evil Wizard sitting on his throne!!!')
    print('you don\' have all the 7 required items in your inventory... This looks bad for you...!!!')
    print('The Evil Wizard stands up from his Throne and with a quick wave of his staff\n'
          'casts a spell and traps you in this dungeon forever!!!')


# Function for the text to print when the player wins the game
def win_text():
    """
    Function contains all the text to be printed when the player encounters the Evil Wizard and has all the 7 items in the inventory.
    :return: None
    """
    print('\nYou see the Evil Wizard sitting on his throne!!!')
    print('\n In a matter of seconds, all the objects in your inventory start flying around you and attaching to your armor one by one!')
    print('\nThe Evil Wizard stands up from his Throne and with a quick wave of his staff\n'
          'casts a spell!!!')
    print('\nBut that spell did nothing to you.')
    print('\nYour armor starts glowing and the magic sword transforms into a guitar')
    print('\nThe Evil Wizard\'s staff reacts to your magic sword and transforms into a guitar')
    print('\n Without a word you both understand what comes next.... AN EPIC GUITAR SOLO BATTLE')
    print('\n You both play your solos and after hours, days, weeks... with no end to it...')
    print('\n You accidentally played the intro to \'Thunderstruck\' by AC/DC')
    print('\n As you play it the Evil Wizard\'s guitar started to break down into pieces')
    print('\n The Evil Wizard falls on his right knee... He lifts his head up and says...')
    print('\n ... I am defeated... You may take the key to exit this dungeon....')
    print('\n You take the key and exit the dungeon, happy with your win you continue on your adventure')
    print('\n The End')


# The main Function that contains everything to run the game
def main():
    """
    Function contain a dictionary of rooms, and a dictionary of rooms with items.
    Then there are 2 functions change_location() and collect_items()
    Both functions are used in the WHILE LOOP where the game runs.
    :return: None
    """
    # Dictionary with all the rooms and nested in each key is the adjacent room
    rooms = {'Dungeon Entrance': {'East': 'The Amethyst Shrine',
                                  'South': 'The Diamond Library'
                                  },
             'The Amethyst Shrine': {'West': 'Dungeon Entrance'
                                     },
             'The Diamond Library': {'North': 'Dungeon Entrance',
                                     'South': 'The Emerald Laboratory',
                                     'West': 'The Music Hall',
                                     'East': 'The Sapphire Foyer'
                                     },
             'The Sapphire Foyer': {'West': 'The Diamond Library'
                                    },
             'The Emerald Laboratory': {'North': 'The Diamond Library',
                                        'East': 'The Ruby Depository',
                                        'South': 'The Rubellite Observatory'
                                        },
             'The Rubellite Observatory': {'North': 'The Emerald Laboratory'
                                           },
             'The Ruby Depository': {'West': 'The Emerald Laboratory'
                                     },
             'The Music Hall': {'East': 'The Diamond Library',
                                'South': 'The Throne Room'
                                },
             'The Throne Room': 'Evil Wizard'
             }

    # Dictionary of all the rooms with items
    room_items = {'The Amethyst Shrine': 'Amethyst Belt',
                  'The Diamond Library': 'Diamond Body Armor',
                  'The Sapphire Foyer': 'Sapphire Helm',
                  'The Emerald Laboratory': 'Emerald Shield',
                  'The Ruby Depository': 'Ruby Boots',
                  'The Rubellite Observatory': 'Rubellite Amulet',
                  'The Music Hall': 'Magic Sword'
                  }

    # Player location (Starting Location)
    location = 'Dungeon Entrance'
    # List of collected items
    collected_items = []
    # Valid inputs to move between rooms
    valid_move_input = ['South', 'West', 'North', 'East']

    # Function used to change player location
    def change_location(current_room, direction_input):
        """
        Function will move the player to the adjacent room.
        Requires the players current location and the direction input.

        :param current_room: str, players current location
        :param direction_input: str, input direction from the player
        :return: str, the new location where the player is
        """
        # From the current room location, move in the direction input by the user
        new_location = rooms[current_room].get(direction_input)
        # Print the new location
        print('\nYou are now in the {room}'.format(room=new_location))
        # Return the new location
        return new_location

    # Function used to collect items
    def collect_items(player_location):
        """
        Function to add item to inventory.
        First it will check if the player is in a room with item,
        IF the room has an item the player will be asked if they want to add that item to their inventory.
        IF no item in the room then print there is nothing.
        IF input is not equal to Yes/No print item disappeared ask them to come back later.
        :param player_location: str, current player location
        :return: None
        """

        # Print the inventory items the player currently has
        print('Inventory Items: {items}'.format(items=collected_items))

        # Check if the player is in a room with item
        if player_location in room_items:
            # Check if that item is not in the players inventory items
            if room_items[player_location] not in collected_items:
                # Ask the player if they want to collect this item
                item_user_input = input('\nYou can collect here the {item} -> Yes/No: \n'.format(item=room_items[player_location])).capitalize()
                # Check if player said Yes
                if item_user_input == 'Yes':
                    # Add the item to player inventory
                    collected_items.append(room_items[player_location])
                    # Print an updated list of player inventory items
                    print('Updated Inventory Item List: {items}\n'.format(items=collected_items))
                # Check if player sain No
                elif item_user_input == 'No':
                    # Print message
                    print('Okay you can come back later to this room and find this item here...')
                # Else the input was invalid print item disappeared
                else:
                    print('The input was not clear you just scared the item away... come back later and you will find it here again')
            # Check IF room item is in the player inventory
            elif room_items[player_location] in collected_items:
                # Print there is nothing in this room
                print('\nThere is nothing in this room...')

    # Call function to display brief description of the game and the rules
    show_story_instructions(location, collected_items)

    # WHILE True no condition is set but contains break points to stop the loop
    while True:
        # Ask the player to input a move save to a variable move_input
        move_input = input('\nEnter your next move: \n').capitalize()

        # Check if player input equals 'Exit'
        if move_input == 'Exit':
            # Call game_over function
            game_over()
            # Break stop and exit the loop
            break
        # Check if the player input move is valid
        elif move_input in valid_move_input:
            # Check if player move input is not in the current location nested keys
            if move_input not in rooms[location].keys():
                # Print there is nothing
                print('There is nothing there, just a wall...')
                # Print player location
                print('You are now in the {location}, try a different direction'.format(location=location))
            # Check If player move input is in the current location nested keys
            elif move_input in rooms[location].keys():
                # Update the location to equal the change_location() function that returns the new location
                location = change_location(location, move_input)
                # Check if player location is the Throne Room
                if location == list(rooms.keys())[-1]:
                    # Print message
                    print('You found the Evil Wizard')
                    # Check IF player has less than 7 items in their inventory
                    if len(collected_items) < 7:
                        # Call defeated_text function will print the text in case the player lost the game
                        defeated_text()
                        # Call game_over function will print game over
                        game_over()
                        # Break stop and exit the loop
                        break
                    # Else the player has 7 items in their inventory
                    else:
                        # Call win_text will print the text in case the player wins the game
                        win_text()
                        # Break stop and exit the loop
                        break
                # Else the player is not in the Throne Room
                else:
                    # Call collect_items function will check for items in that room
                    collect_items(location)
        # Check if the player input move is not valid
        elif move_input not in valid_move_input:
            # Print invalid move input
            print('Um... Invalid move input')
            # Print a list of valid move inputs
            print('To move between rooms type: {}'.format(', '.join(valid_move_input)))
            # Print the current player location
            print('You are now in the {location}'.format(location=location))

        # Print in morse code 'The Evil Wizard Dungeon'
        print('\n- .... .   . ...- .. .-..    .-- .. --.. .- .-. -..    -.. ..- -. --. . --- -. ')


# Run directly by the python interpreter
if __name__ == '__main__':
    # Call main() function to run the game
    main()
