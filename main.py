from rooms import rooms_id
import player
import game_functions as gf    # all functions are referred as 'gf' now
import game_content as gc    # all dialogue are referred as 'gc' now
import pygame
import os

# These variables are to be global
current_room = rooms_id['lobby']
current_dialogue = gc.opening_dialogue['description']


# all game loops and events are tested and ran here
# main game loop
def game():
    print(items.item_note['Title'])
    pygame.mixer.init()
    pygame.mixer.music.load("8bit.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    while True:
        # this is just a test to see if this function can run
        gf.print_dialogue(current_dialogue)
        gf.print_room(current_room)
        gf.print_inventory(player.inventory)
        gf.main()
        os.system('cls')
        # don't take out
        break


if __name__ == '__main__':
    game()

#test
