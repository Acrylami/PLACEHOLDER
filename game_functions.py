# all game functions will be placed in this file
import rooms
import game_content as gc  # game_content is referred as 'gc'
from player import *
from items import items_id
from main import current_dialogue, current_room  # global variables to update
import string
import pygame


def print_room():
    """Will take a room as an argument, and display all of its contents"""
    global current_room
    print()
    print('You are in the ' + current_room['name'].upper())
    print()


def print_dialogue():
    """Will take a form of dialogue as an argument, and display it properly"""
    global current_dialogue
    print()
    print(current_dialogue.upper())
    print()


def exit_leads_to(exits, direction):
    """This will take a dictionary of exits, and a direction from the user"""
    return exits[direction]['name']


def is_exit_valid(exits, direction):
    if direction in exits:
        return True
    return False


def move(exits, direction):
    return rooms.rooms_id[exits[direction]]


def print_room_items(room):
    """Will take room item(s) as an argument, and will output them properly"""
    print()
    print('You find in the room ' + room['items'])


def print_inventory(inventory):
    """Will take the player's inventory and print out the items names'"""
    store_string = ''
    for value in inventory:
        if value == inventory[-1]:
            store_string = store_string + value['name'] + '.'
            break
        store_string = store_string + value['name'] + ', '
    print('You have: ' + store_string)


def no_whitespace(text):
    """will remove beginning and trailing whitespace from input"""
    return text.strip()


def no_punct(text):
    """will remove all forms of punctuation that is in the text"""
    punctuation = string.punctuation
    for letter in text:
        if letter in punctuation:
            text = text.replace(letter, '')
    return text


def refine_words(text):
    """Compare the user input with the text document, if both words do no
    appear, then add that word from user input to the filtered list"""

    with open('stop.txt', 'r') as f_obj:
        skip = f_obj.readlines()
        skip = ''.join(skip)
        skip = skip.split('\n')
        words_wanted = []
        for item in text:
            if not (item in skip):
                words_wanted.append(item)
        return words_wanted


def normal_input(user_input):
    """Will take the user input and firstly remove punctuation, then the
    whitespace and then lastly return it as a list, so it can therefore be
    processed in execute command"""
    user_input = no_punct(user_input)
    user_input = no_whitespace(user_input)
    normal_lst = user_input.split()
    filtered = refine_words(normal_lst)
    return filtered


def exe_go(direction):
    """when given the direction, this function will move the player to the
    room in question, and the room which the player is currently in will be
    the new current room"""
    global current_room
    footsteps = pygame.mixer.Sound("Footsteps.ogg")
    exit = is_exit_valid(current_room['exits'], direction)
    room_door = current_room['exits'][direction]
    try:
        if rooms.rooms_id[room_door]['door']:
            if exit:
                footsteps.set_volume(0.8)
                footsteps.play()
                current_room = move(current_room['exits'], direction)
            else:
                print("You cannot go there.")
        else:
            print('The door is locked. You need a key')
    except KeyError:
        pass


def exe_take(item_id):
    """given the item id, the player can pickup objects from the room,
    and this will be added to the player inventory, and removed from the
    current room items"""
    global current_room
    global inventory
    pickup_sound = pygame.mixer.Sound("pickupsound.ogg")

    try:
        item_in_room = items_id[item_id]

        if current_room['items']:
            item_lst = current_room['items']

            if item_in_room not in item_lst:
                print('You cannot take this')

            for item in item_lst:
                if item == item_in_room:
                    pickup_sound.set_volume(0.3)
                    pickup_sound.play()
                    inventory.append(item)
                    current_room['items'].remove(item)

    except KeyError:
        print('You cannot take this')


def exe_interact(user_input_command):
    """This function will allow the player to interact with objects within a
    room and if they managed to solve the riddle by interacting with the
    right item, then one of four keys will be appended to their inventory,
    this will only work for the items that we have coded in here"""
    global inventory
    global current_dialogue
    pickup_note = pygame.mixer.Sound("note.ogg")
    if user_input_command == "candle":
        if items.item_matchsticks in inventory:
            if user_input_command == items.item_riddle_candle['name']:
                items.item_riddle_candle['on'] = True
                if items.item_riddle_candle['on']:
                    inventory.append(items.item_key_1)
                else:
                    inventory.append(items.item_key_1)
        else:
            print("You don'\t have anything to light the candle with.")

    elif user_input_command == "note":
        if items.item_note1 in inventory:
            if user_input_command == items.item_note1['name']:
                gc.current_riddle = items.item_note1['riddle_1']
                pickup_note.play()
        else:
            print("You don'\t have a note")


def exe_observe(user_input_command):
    """This function will allow the player to examine the item, it will
    essentially output the item description to the user"""
    global inventory
    global items

    try:
        if inventory:
            item_to_observe = items_id[user_input_command]
            print(item_to_observe['description'])
    except KeyError:
        print('You cannot observe this')


def exe_command(user_input_lst):
    """function will check the first item, in which it will then either call
    go, take or solve riddle"""
    if len(user_input_lst) == 0:
        return None

    if user_input_lst[0] == 'go':
        if len(user_input_lst) > 1:
            exe_go(user_input_lst[1])
        else:
            print('Go to which room?')

    elif user_input_lst[0] == 'take':
        if len(user_input_lst) > 1:
            exe_take(user_input_lst[1])
        else:
            print('Take which item?')

    elif user_input_lst[0] == 'interact':
        if len(user_input_lst) > 1:
            exe_interact(user_input_lst[1])
        else:
            print('Your answer to your the riddle?')
    elif user_input_lst[0] == 'observe':
        if len(user_input_lst) > 1:
            exe_observe(user_input_lst[1])
        else:
            print('Observe which item?')

    else:
        print('What are you doing?')


def print_menu():
    """Will output the items in the room and also the player's inventory"""

    print("\nThere is in this room: ")

    for values in current_room['items']:
        print(values.get('name'))

    print('\nYou can: ')
    for direction, exit in current_room['exits'].items():
        print('GO ' + direction + ' to ' + exit)

    if gc.current_riddle != items.item_title['Instructions']:
        print(gc.current_riddle)

    if items.item_key_1 in inventory:
        print("\n" + items.item_riddle_candle['description_2'])
        print(items.item_key_1['description'])


def main():
    """Function will display the options the user has, it will then read
    their input and go on to to the parser where their input will be
    corrected for the exe commands to work correctly"""
    # display the menu to the player
    # take the user input
    user_input = input('>')

    # normal the input
    normal_user_input = normal_input(user_input)

    exe_command(normal_user_input)
