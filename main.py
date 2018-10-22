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
current_dialogue = gc.opening_dialogue['description']
background_music = pygame.mixer.Sound("OST.ogg")


# all game loops
# and events are tested and ran here
# main game loop
def game():

    print(items.item_title['Title'])
    input("""\n\t\t\t\t\t\t\t\t  PRESS ENTER TO CONTINUE""")
    os.system('cls')
    print(gc.opening_dialogue['description'])
    input('\n\t\t\t\t\t\t\t\t  PRESS ENTER TO CONTINUE')
    os.system('cls')
    print("\n\t\t\t\t\t\tYou have a note in your pocket, "
          "TYPE 'interact note' to see your first riddle.")
    gf.main()
    os.system('cls')
    background_music.set_volume(0.5)
    background_music.play(-1)

    while True:
        # this is just a test to see if this function can run
        print(items.item_title['Title'])
        if gc.current_riddle == items.item_title['Instructions']:
            print(gc.current_riddle)
        gf.print_dialogue()
        gf.print_inventory(player.inventory)
        gf.print_room()
        gf.print_menu()
        gf.main()
        input('PRESS ENTER TO CONTINUE')
        os.system('cls')

        # don't take out


if __name__ == '__main__':
    game()

#test
