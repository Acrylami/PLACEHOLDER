def exe_take(item_id):
    """given the item id, the player can pickup objects from the room,
    and this will be added to the player inventory, and removed from the
    current room items"""
    global current_room
    global inventory
    pickup_sound = pygame.mixer.Sound("pickupsound.ogg")

    try:
        item_in_room = items_id[item_id]

        if item_in_room == items.item_light_switch:
            print('You cannot take this.')
            return

        if item_in_room == items.item_pendulum:
            if items.item_key_3 not in inventory:
                print("I don't think I need this yet...")
                return

        if item_in_room == items.item_building_block:
            if items.item_key_2 not in inventory:
                print("I don't think I need this yet...")
                return

        if item_in_room == items.item_riddle_candle:
            print("It has no use to me, if it is not lit up")

        if item_in_room == items.item_button:
            print('you cannot take this.')
            return

        if current_room['items']:
            item_lst = current_room['items']

            if item_in_room not in item_lst:
                print('You cannot take this.')

            for item in item_lst:
                if item == item_in_room:
                    pickup_sound.set_volume(0.3)
                    pickup_sound.play()
                    inventory.append(item)
                    current_room['items'].remove(item)

    except KeyError:
        print('You cannot take this.')


def exe_interact(user_input_command):
    """This function will allow the player to interact with objects within a
    room and if they managed to solve the riddle by interacting with the
    right item, then one of four keys will be appended to their inventory,
    this will only work for the items that we have coded in here"""
    global inventory
    global current_dialogue
    global has_printed_1
    global rooms
    global items
    pickup_note = pygame.mixer.Sound("note.ogg")
    matchstick_sound = pygame.mixer.Sound("matchstick.ogg")
    got_key = pygame.mixer.Sound("got_key.ogg")
    mirror = pygame.mixer.Sound("mirror.ogg")
    if user_input_command == "candle":
        if items.item_riddle_candle in current_room['items']:
            if items.item_matchsticks in inventory:
                if items.item_riddle_candle in current_room['items'] or inventory:
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
                print(print("You don't have anything to light the candle with."))
        else:
            print("...")

    elif user_input_command == "note":
        if items.item_note1 in inventory:
            if user_input_command == items.item_note1['name']:
                gc.current_riddle = items.item_note1['riddle_1']
                pickup_note.play()
            else:
                print("You don't have a note")
        else:
            print('...')

    elif user_input_command == 'switch':
        if items.item_light_switch in current_room['items']:
            items.item_light_switch['switch'] = False
            print(items.item_light_switch['description_2'])
            rooms.room_nursery['items_not'].append(items.item_button)
            items.item_button['on'] = True
        else:
            print('...')

    elif user_input_command == 'button':
        if items.item_button in current_room['items']:
            if items.item_button['on']:
                inventory.append(items.item_key_2)
                got_key.play()
                rooms.room_bathroom['door'] = True
            else:
                print('...')
        else:
            print('...')

    elif user_input_command == 'clock':
        if items.item_riddle_clock in current_room['items']:
            if items.item_pendulum in inventory:
                if user_input_command == items.item_riddle_clock['name']:
                    inventory.append(items.item_key_4)
                    got_key.play()
                    rooms.room_main_door['door'] = True
            else:
                print("This clock is missing something...")
        else:
            print('...')

    elif user_input_command == 'mirror':
        if items.item_mirror in current_room['items']:
            if (items.item_paper not in inventory) and (
                    items.item_building_block not in inventory):
                print("You see your reflection")
            elif (items.item_paper in inventory) and (
                    items.item_building_block not in inventory):
                print(items.item_paper['description_2'])
            elif items.item_paper and items.item_building_block in inventory:
                mirror.set_volume(0.4)
                mirror.play()
                time.sleep(1.5)
                inventory.append(items.item_key_3)
                got_key.play()
                rooms.room_kitchen['door'] = True

            else:
                print('You cannot interact with this')
        else:
            print('...')

