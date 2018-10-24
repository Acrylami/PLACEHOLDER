import rooms, player, items
import game_functions as gf    # all functions are referred as 'gf' now
import game_content as gc    # all dialogue are referred as 'gc' now
import pygame
import os
import time


# These variables are to be global
current_room = rooms.rooms_id['lobby']
pygame.mixer.init()
current_dialogue = gc.filler_dialogue['description'].upper()
background_music = pygame.mixer.Sound("OST.ogg")
scream = pygame.mixer.Sound("scream.ogg")
last_output = ""
terminal_width = os.get_terminal_size().columns
pickup_note = pygame.mixer.Sound("note.ogg")

# all game loops
# and events are tested and ran here
# main game loop
def game():
    # print title of game
    os.system('cls')
    gf.print_centered(items.item_title['Title'], False)
    enter = 'PRESS ENTER TO CONTINUE'
    input(enter.center(terminal_width))
    os.system('cls')

    # print the opening dialogue of game

    gf.print_centered(gc.opening_dialogue['description'], False)
    input(enter.center(terminal_width))
    os.system('cls')
    
    # ask the user for first help
    s = "TYPE 'help' to see the game instructions"
    print("\n\n\n\n\n\n\n\n\n\n" + s.center(terminal_width))
    #print("\033[" + str(int(terminal_width/2)) + ";H")
    user_input = input('> ')
    gf.get_help(user_input)
    print("You can TYPE 'help' anytime to see the game instructions".center(terminal_width))
    input(enter.center(terminal_width))
    os.system('cls')

    # ask the user to do their first interact
    s = "You have a note in your pocket, TYPE 'interact note' to see your first riddle."
    print("\n\n\n\n\n\n\n\n\n\n" + s.center(terminal_width))
    user_input = input('>')
    gf.interact_note(user_input)
    os.system('cls')

    # play the music once game before main game loop
    background_music.set_volume(0.5)
    background_music.play(-1)

    while True:
        # print the title of the game
        print_startscreen = items.item_title['Title'].split('\n')
        for x in print_startscreen:
            print(x.center(terminal_width))

        # print the dialogue for user events
        gf.print_dialogue()

        # show player their inventory
        gf.print_inventory(player.inventory)

        # output which room their in
        gf.print_room()

        # output the contents of the room, and if they earned a key
        gf.print_menu()

        # checks for user input, and is a parser
        gf.main_input()

        # checks to see if the user has opened the door, the user has won
        # the game
        if rooms.rooms_id['main door']['opened']:
            print(items.item_paper['description_3'])
            scream.set_volume(1)
            scream.play()
            time.sleep(4)
            break

        # clear the screen after each run
        os.system('cls')


if __name__ == '__main__':
    game()
