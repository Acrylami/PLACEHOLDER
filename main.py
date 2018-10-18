from rooms import rooms_id
import player
import game_functions as gf    # all functions are referred as 'gf' now
import game_content as gc    # all dialogue are referred as 'gc' now
import items
import pygame
import os


# These variables are to be global
current_room = rooms_id['lobby']
pygame.mixer.init()
current_dialogue = gc.opening_dialogue['description']
background_music = pygame.mixer.Sound("8bit.ogg")


# all game loops
# and events are tested and ran here
# main game loop
def game():
    background_music.set_volume(0.5)
    background_music.play()
    while True:
        # this is just a test to see if this function can run
        print(items.item_note['Title'])
        gf.print_dialogue()
        gf.print_room()
        gf.print_inventory(player.inventory)
        gf.main()
        os.system('cls')
        # don't take out


if __name__ == '__main__':
    game()

#test
