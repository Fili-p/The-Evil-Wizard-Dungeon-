# The Evil Wizard Dungeon

## Overview
**The Evil Wizard Dungeon** is a Python-based text adventure game where players navigate a dungeon, and ultimately face the evil wizard. This project was created as part of IT-140 scripting class to practice Python fundamentals.

## Features
- Interactive command-line gameplay
- Dungeon exploration
- Inventory system to collect items
---

## Story and Map Description
This tale tells the story of a young man who sails out to sea in search of unknown lands, adventures, and treasure. In his small boat, Ron finally sees land after drifting on water for three days and three nights. As he stared out at the island, he could see no more than a small beach with a few trees and a mountain. Once he had anchored his boat on the beach, Ron was eager to begin exploring, so he immediately headed in the direction of the mountain. While he was on his way, he stumbled upon an underground cave. Unlike natural caves, this one was carved by someone. Since Ron is an experienced treasure hunter and explorer, he enters the cave without fear. Upon entering the cave, Ron finds a torch. As soon as he lit it, the cave entrance closed. A written message was displayed on the wall in front of him.

"The only way out of this dungeon is to defeat the evil with the key that is in The Throne Room. To accomplish this you first must uncover the dungeon secrets and collect all 7 items that will help you defeat the Evil Wizard. The items are, the amethyst belt in the Amethyst Shrine, the diamond body armor in the Diamond Library, the ruby boots in the Ruby Depository, the sapphire helm in the Sapphire Foyer, the emerald shield in the Emerald Laboratory, the rubellite amulet in the Rubellite Observatory, the magic sword in the Music Hall. After you have gathered all of these items, proceed directly to the Throne Room where you will find the Evil Wizard."

## Game Map
<img width="937" height="862" alt="game_map" src="https://github.com/user-attachments/assets/0ef26189-ff8a-497a-907e-2f9bd111a292" />

---

## Note:
The pseudocode explains how the player moves between rooms and collects items. Black color font is used to write the code logic responsible for moving and updating the player's location. The pseudocode consists of two main FUNCTIONS, one for changing the location of the player and one for collecting items. All game functions will run inside a WHILE LOOP. Certain conditions will be used to break the loop if the player wins or loses.

## Pseudocode
```text
Pseudocode: 
Create a DICTIONARY with the rooms and nested in each room is the adjacent room with key as direction and value is the room

Create a DICTIONARY with rooms_with_item, the key is the room and value is the item in that room

Create a variable player_location set it equal to the starting room
Create a LIST of collected_items set it equal to an empty list
Create a variable game_on and set it equal to TRUE

PRINT Welcome message and Game Rules
PRINT You are now in the (player starting room) and the first 2 move options East and South
PRINT collected_items LIST


FUNCTION change_location requires 2 parameters (player_location, move_input):
    Create a variable new_location equals room player_location move to the direction move_input
    PRINT the players new_location
    RETURN new_location
ENDFUNCTION


FUNCTION collect_items requires 1 parameter (player_location):
    PRINT the collected_items list

    IF the player_location is in the rooms_with_item:
        IF room item is not in the collected_items LIST:
            INPUT ask the player if he want to pick that item and save to a variable item_user_input
            IF item_user_input equals Yes:
                ADD the item to the collected_items LIST
                PRINT the updated LIST of collected_items
        ELIF room item is in the collected_items list:
            PRINT there is nothing in this room
    ENDIF
ENDFUNCTION
WHILE LOOP game_on is equal to TRUE:
    INPUT Ask the user to enter a direction to move save it to a variable named move_input

    IF move_input is not in the rooms dictionary player_location nested keys:
        PRINT invalid direction input
    ELIF move_input is in the rooms dictionary player_location nested keys:
        IF player_location doesn't equal the Evil Wizard room:
            player_location equals change_location FUNCTION (player_location, move_input)
            IF player_location equals the Evil Wizard room:
                PRINT You found the Evil Wizard
                IF the collected_items LIST has less then seven items:
                    PRINT You are defeated
                    Set game_on to equal FALSE
                    BREAK stop the loop and exit
                ELSE the collected_items list equals to seven items:
                    PRINT You defeated the Evil Wizard
                    Set game_on to equal FALSE
                    BREAK stop the loop and exit
            ELSE player_location doesn't equal Evil Wizard room:
                CALL collected_items FUNCTION with the argument (player_location)
    ENDIF
ENDWHILE
```
## Python Code
<a href="https://github.com/Fili-p/The-Evil-Wizard-Dungeon-/blob/main/The_Evil_Wizard_Dungeon.py">
The Evil Wizard Dungeon
</a>

---
## Learning Outcomes
- Practiced Python programming concepts: loops, conditionals, functions, and data structures  
- Gained experience with handling user input and implementing game logic  
- Developed skills in designing interactive storylines with branching paths  













