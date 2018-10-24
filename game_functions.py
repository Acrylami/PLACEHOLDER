# all game functions will be placed in this file
import rooms
import game_content as gc  # game_content is referred as 'gc'
from player import *
from items import items_id
import main
import string
import pygame
import time


def print_room():
    """Will take a room as an argument, and display all of its contents"""
    print()
    print('You are in the ' + main.current_room['name'].upper())
    print(main.current_room['description'].upper())


def print_dialogue():
    """Will take a form of dialogue as an argument, and display it properly"""
    print()
    print(main.current_dialogue.upper())
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
    footsteps = pygame.mixer.Sound("Footsteps.ogg")
    opened = pygame.mixer.Sound("open.ogg")
    locked = pygame.mixer.Sound("locked.ogg")
    exit = is_exit_valid(main.current_room['exits'], direction)
    try:
        room_door = main.current_room['exits'][direction]
        if main.current_room['exits'][direction] != 'main door':
            if rooms.rooms_id[room_door]['door']:
                if exit:
                    if direction == 'up' or direction == 'down':
                        footsteps.set_volume(0.8)
                        footsteps.play()
                        main.current_room = move(main.current_room['exits'],
                                                 direction)
                    else:
                        opened.set_volume(0.8)
                        opened.play()
                        time.sleep(2)
                        footsteps.set_volume(0.8)
                        footsteps.play()
                        main.current_room = move(main.current_room['exits'],
                                                 direction)
                else:
                    main.last_output = "You cannot go there."
            else:
                locked.set_volume(0.8)
                locked.play()
                main.last_output = "The door is locked. You need a key"

        else:
            if rooms.rooms_id[room_door]['door'] == True:
                opened.set_volume(0.8)
                opened.play()
                time.sleep(2)
                rooms.room_main_door['opened'] = True
            else:
                locked.set_volume(0.8)
                locked.play()
                main.last_output = 'The door is locked. You need a key'
    except KeyError:
        main.last_output = 'You cannot go there.'


def exe_take(item_id):
    """given the item id, the player can pickup objects from the room,
    and this will be added to the player inventory, and removed from the
    current room items"""
    global inventory
    pickup_sound = pygame.mixer.Sound("pickupsound.ogg")

    try:
        item_in_room = items_id[item_id]

        if item_in_room == items.item_light_switch:
            main.last_output = 'You cannot take this.'
            return

        if item_in_room == items.item_pendulum:
            if items.item_key_3 not in inventory:
                main.last_output = "I don't think I need this yet..."
                return

        if item_in_room == items.item_building_block:
            if items.item_key_2 not in inventory:
                main.last_output = "I don't think I need this yet..."
                return

        if item_in_room == items.item_riddle_candle:
            main.last_output = "It has no use to me, if it is not lit up"
            return

        if item_in_room == items.item_button:
            main.last_output = 'you cannot take this.'
            return

        if main.current_room['items']:
            item_lst = main.current_room['items']

            if item_in_room not in item_lst:
                main.last_output = 'You cannot take this.'

            for item in item_lst:
                if item == item_in_room:
                    pickup_sound.set_volume(0.3)
                    pickup_sound.play()
                    inventory.append(item)
                    main.current_room['items'].remove(item)

    except KeyError:
        main.last_output = 'You cannot take this.'


def exe_interact(user_input_command):
    """This function will allow the player to interact with objects within a
    room and if they managed to solve the riddle by interacting with the
    right item, then one of four keys will be appended to their inventory,
    this will only work for the items that we have coded in here"""
    global inventory
    global has_printed_1
    global rooms
    global items
    pickup_note = pygame.mixer.Sound("note.ogg")
    matchstick_sound = pygame.mixer.Sound("matchstick.ogg")
    got_key = pygame.mixer.Sound("got_key.ogg")
    mirror = pygame.mixer.Sound("mirror.ogg")
    clock = pygame.mixer.Sound("clock.ogg")
    if user_input_command == "candle":
        if items.item_riddle_candle in main.current_room['items']:
            if items.item_matchsticks in inventory:
                if items.item_riddle_candle in main.current_room[
                    'items'] or inventory:
                    if user_input_command == items.item_riddle_candle['name']:
                        items.item_riddle_candle['on'] = True
                        if items.item_riddle_candle['on']:
                            inventory.append(items.item_key_1)
                            rooms.room_nursery['door'] = True
                            matchstick_sound.set_volume(1)
                            matchstick_sound.play()
                            time.sleep(5)
                            got_key.set_volume(0.8)
                            got_key.play()
                        else:
                            inventory.append(items.item_key_1)
                            rooms.room_nursery['door'] = True
                            matchstick_sound.set_volume(1)
                            matchstick_sound.play()
            else:
                main.last_output = "You don't have anything to light the candle with."
        else:
            main.last_output = "..."

    elif user_input_command == "note":
        if items.item_note1 in inventory:
            if user_input_command == items.item_note1['name']:
                gc.current_riddle = items.item_note1['riddle_1']
                pickup_note.play()
            else:
                main.last_output = "You don't have a note"
        else:
            main.last_output = '...'

    elif user_input_command == 'switch':
        if items.item_light_switch in main.current_room['items']:
            items.item_light_switch['switch'] = False
            if len(rooms.room_nursery['items_not']) > 2:
                main.last_output = 'The glowing button should be pressed...'
                items.item_button['on'] = True
            else:
                main.last_output = items.item_light_switch['description_2']
                rooms.room_nursery['items_not'].append(items.item_button)
                items.item_button['on'] = True
        else:
            main.last_output = '...'

    elif user_input_command == 'button':
        if items.item_button in main.current_room['items_not']:
            if items.item_button['on']:
                inventory.append(items.item_key_2)
                got_key.play()
                rooms.room_bathroom['door'] = True
            else:
                main.last_output = '...'
        else:
            main.last_output = '...'

    elif user_input_command == 'clock':
        if items.item_riddle_clock in main.current_room['items']:
            if items.item_pendulum in inventory:
                if user_input_command == items.item_riddle_clock['name']:
                    clock.set_volume(0.8)
                    clock.play()
                    time.sleep(3)
                    inventory.append(items.item_key_4)
                    got_key.play()
                    rooms.room_main_door['door'] = True
            else:
                main.last_output = "This clock is missing something..."
        else:
            main.last_output = '...'

    elif user_input_command == 'mirror':
        if items.item_mirror in main.current_room['items']:
            if (items.item_paper not in inventory) and (
                    items.item_building_block not in inventory):
                main.last_output = "You see your reflection"
            elif (items.item_paper in inventory) and (
                    items.item_building_block not in inventory):
                main.last_output = items.item_paper['description_2']
            elif items.item_paper and items.item_building_block in inventory:
                mirror.set_volume(0.4)
                mirror.play()
                time.sleep(1.5)
                inventory.append(items.item_key_3)
                got_key.play()
                rooms.room_kitchen['door'] = True

            else:
                main.last_output = 'You cannot interact with this'
        else:
            main.last_output = '...'


def exe_observe(user_input_command):
    """This function will allow the player to examine the item, it will
    essentially output the item description to the user"""
    global inventory

    try:
        item_to_observe = items_id[user_input_command]

        if item_to_observe in inventory:
            main.last_output = item_to_observe['description']

        elif item_to_observe in main.current_room['items']:
            main.last_output = item_to_observe['description']

        elif item_to_observe in main.current_room['items_not']:
            main.last_output = item_to_observe['description']

        else:
            main.last_output = 'You cannot observe this'
    except KeyError:
        main.last_output = 'You cannot observe this'


def get_help(user_input):
    """Player type 'help' to see the instructions whenever they want"""
    while user_input != 'help':
        print("You need to type in 'help' to see the game instructions")
        user_input = input('>')
    else:
        print(items.item_title['Instructions'])


def exe_help():
    pickup_note = pygame.mixer.Sound("note.ogg")
    pickup_note.play()
    main.last_output = items.item_title['Instructions']


def exe_command(user_input_lst):
    """function will check the first item, in which it will then either call
    go, take or solve riddle"""
    if len(user_input_lst) == 0:
        return None

    if user_input_lst[0] == 'go':
        if len(user_input_lst) > 1:
            exe_go(user_input_lst[1])
        else:
            main.last_output = 'Go to which room?'

    elif user_input_lst[0] == 'take':
        if len(user_input_lst) > 1:
            exe_take(user_input_lst[1])
        else:
            main.last_output = 'Take which item?'

    elif user_input_lst[0] == 'interact':
        if len(user_input_lst) > 1:
            exe_interact(user_input_lst[1])
        else:
            main.last_output = 'Your answer to the riddle?'
    elif user_input_lst[0] == 'observe':
        if len(user_input_lst) > 1:
            exe_observe(user_input_lst[1])
        else:
            main.last_output = 'Observe which item?'
    elif user_input_lst[0] == 'help':
        if len(user_input_lst) == 1:
            exe_help()
        else:
            main.last_output = "You must type only 'help' to show the instructions"

    else:
        main.last_output = 'What are you doing?'


def interact_note(user_input):
    """Function specific for the opening dialogue"""

    while user_input != 'interact note':
        print("You need to type in 'interact note' to see your first riddle")
        user_input = input('>')
    else:
        exe_interact('note')


def print_menu():
    """Will output the items in the room and also the player's inventory"""
    global has_printed_1
    global has_printed_2
    global has_printed_3
    global has_printed_4

    print("\nThere is in this room: ")

    for values in main.current_room['items']:
        print(values.get('name'))

    if main.current_room['items_not']:
        for values in main.current_room['items_not']:
            if values == items.item_button:
                if items.item_light_switch['switch'] == False:
                    print(values.get('name'))
            else:
                print(values.get('name'))

    print('\nYou can: (go/take/interact/observe/help)')
    for direction, exit in main.current_room['exits'].items():
        if rooms.rooms_id[exit]['door']:
            print('GO ' + direction + ' to ' + exit)
        else:
            print('GO ' + direction + ' to ' + exit + " (LOCKED)")

    if gc.current_riddle != items.item_title['Instructions']:
        print(gc.current_riddle)

    print(main.last_output)
    main.last_output = ""

    if (items.item_key_1 in inventory) and not (has_printed_1):
        print("\n" + items.item_riddle_candle['description_2'])
        print(items.item_key_1['description'])
        has_printed_1 = True
        gc.current_riddle = items.item_note1['riddle_2']

    if (items.item_key_1 and items.item_key_2) in inventory and not (
            has_printed_2):
        print('\n' + items.item_button['description_2'])
        print(items.item_key_2['description'])
        has_printed_2 = True
        gc.current_riddle = items.item_note1['riddle_3']

    if (items.item_key_3 in inventory) and not (has_printed_3):
        print("\n" + items.item_key_3['description'])
        has_printed_3 = True

    if (items.item_key_4 in inventory) and not (has_printed_4):
        print("\n" + items.item_riddle_clock['description_2'])
        print(items.item_key_4['description'])
        has_printed_4 = True


def main_input():
    """Function will display the options the user has, it will then read
    their input and go on to to the parser where their input will be
    corrected for the exe commands to work correctly"""
    # display the menu to the player
    # take the user input
    user_input = input('>')

    # normal the input
    normal_user_input = normal_input(user_input)

    exe_command(normal_user_input)
