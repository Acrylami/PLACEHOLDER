from rooms import rooms_id
import player
import game_functions as gf    # all functions are referred as 'gf' now
import game_content as gc    # all dialogue are referred as 'gc' now
import items
import pygame
import os
import time


# These variables are to be global
current_room = rooms_id['lobby']
pygame.mixer.init()
current_dialogue = gc.filler_dialogue['description']
background_music = pygame.mixer.Sound("OST.ogg")


# all game loops
# and events are tested and ran here
# main game loop
def game():
    # print title of game
    os.system('cls')
    print(items.item_title['Title'])
    s = "PRESS ENTER TO CONTINUE"
    input(s.center(44))
    os.system('cls')

    # print the opening dialogue of game
    print(gc.opening_dialogue['description'])
    input(s.center(70))
    os.system('cls')

    # ask the user for first help
    print("\n\n\n\n\n\n\n\n\n\n"
    "TYPE 'help' to see the game instructions")
    user_input = input('> ')
    gf.get_help(user_input)
    print("You can TYPE 'help' anytime to see the game instructions")
    input('PRESS ENTER TO CONTINUE')
    os.system('cls')

    # ask the user to do their first interact
    print("\n\n\n\n\n\n\n\n\n\nYou have a note in your pocket, "
          "TYPE 'interact note' to see your first riddle.")
    user_input = input('>')
    gf.interact_note(user_input)
    os.system('cls')

    # play the music once game before main game loop
    background_music.set_volume(0.5)
    background_music.play(-1)

    while True:

        # print the title of the game
        print(items.item_title['Title'])

        # print the dialogue for user events
        gf.print_dialogue()

        # show player their inventory
        gf.print_inventory(player.inventory)

        # output which room their in
        gf.print_room()

        # output the contents of the room, and if they earned a key
        gf.print_menu()

        # checks for user input, and is a parser
        gf.main()

        # checks to see if the user has opened the door, the user has won
        # the game
        if rooms_id['main door']['opened']:
            print('CONGRATULATIONS')
            break

        input('PRESS ENTER TO CONTINUE')


        # clear the screen after each run
        os.system('cls')


if __name__ == '__main__':
    game()
