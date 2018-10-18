# all game functions will be placed in this file
import rooms
import game_content as gc    # game_content is referred as 'gc'
import player
import items
from main import current_dialogue, current_room    # global variables to update
import string


def print_room(room):
    """Will take a room as an argument, and display all of its contents"""
    print()
    print('You are in the ' + room['name'].upper())
    print()


def print_dialogue(dialogue):
    """Will take a form of dialogue as an argument, and display it properly"""
    print()
    print(dialogue.upper())
    print()


def exit_leads_to(exits, direction):
    """This will take a dictionary of exits, and a direction from the user"""
    return exits[direction]['name']


def is_exit_valid(exits, direction):
    if direction in exits:
        return exits[direction]


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
    disposable_words = [
        'a', 'aa', 'aaa',  'an', 'and', 'the', 'be', 'to', 'of', 'in', 'that',
        'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do',
        'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her',
        'she', 'or', 'will', 'my', 'one', 'all' , 'would', 'there', 'their',
        'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'me',
        'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know',
        'take', 'people', 'into', 'year', 'good', 'some', 'could', 'them',
        'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its',
        'over', 'think', 'also', 'back', 'after', 'two', 'how', 'our', 'work',
        'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any',
        'these', 'give', 'day', 'most', 'us',
    ]

    with open('stop.txt', 'r') as f_obj:

        words_wanted = []
        for item in text:
            if item not in disposable_words:
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


def exe_go(user_input_command):
    pass


def exe_take(user_input_command):
    pass


def exe_solve_riddle(user_input_command):
    pass


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

    elif user_input_lst[0] == 'solve':
        if len(user_input_lst) > 1:
            exe_solve_riddle(user_input_lst[1])
        else:
            print('Your answer to your the riddle?')

    else:
        print('What are you doing?')


def riddle_1():
    x = input("I'm tall when I'm young and I'm short when I'm old. What am I?")
    if x == "candle" or "a candle":
        pass
"""    
def take():
    #take key and display:
    
    print("")
    print("                      :sdmNNNds/`                                                                           ")
    print("                    -dMNho//oyNMm/                                                                          ")
    print("                   -NMd-      .yMM/                                                                         ")
    print("                   oMM:        `MMh                                                                         ")
    print("             `:oyhhmMMs        :MMy                                                                         ")
    print("           `omMNdhhmMMm:    .-sNMd--`.oo:                                                                   ")
    print("           oMMh-   `:+.`sdyomMMMNdNMdmMMMoooooooooooo++++++oooooooooooooooooooooooooooooooooooooooo+-oso.   ")
    print("           dMM-        /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMh   ")
    print("           +MMh-`  `:+.`sdyomMMMNdNMdmMMMooooooooooooooooooooosssssssssssssssssssssssssdMMMMMMmyssys/yhs-   ")
    print("            +mMNdhhmMMm:    .-sNMd--`.oo:                                         yyyyydMMMMMMmyyyyy`       ")
    print("             `:oyyymMMo        /MMs                                              `dNMMMMMMMMMMMMMMNd`       ")
    print("                   sMM:        `MMh                                               /dMMMMMMMMMMMMMMd+`       ")
    print("                   -NMd-      .hMM/                                              `MMMMNyyMMMMyyNMMMM.       ")
    print("                    -dMNho//ohNMm/                                               `MMMMm  NMMM  dMMMM.       ")
    print("                      :sdmNNNds/`                                                `mmmmh  dmmm  ymmmm`       ")
    print("")
    print("    ")
    print("   ")
    print("   ")
    print("                                                       ")                                        
    print("                                                        ")                                       
    print("        `:`   :`  -/+/-   --    :`      `://:`   .://-  .//////.     `:.      `:   :` :////`--   --  s.   ")  
    print("         od` sy .do-.-sd` sy    N:    `yy:..:/  yh-..+m-`.-yh..`    +om+      /m -h+  mo--- -m: :m.  N-    ") 
    print("          +dsy  sh     m/ sy    N:    +d  .--- :N`    sh   sy         d+      /Nsy`   my++:  .m+m.   N-   ")  
    print("           sd   sh     N/ sy    N:    +m  .-od :N`    yy   sy         d+      /m:d/   m+``    -M-    m.    ") 
    print("           oh   .ds:-/hs  -m+-:sh      sh+::yd  sh/-:sh`   sy       -:ds:`    /m `sh. ms:::`  .M`   `o.     ")
    print("           `.     .::-`     -::`         -::.    `-:-`     ..       -----`    `.   .. .----`   -     :`   ")  
        

"""


def print_menu():
    """Will output the items in the room and also the player's inventory"""
    print("You can:")
    for values in current_room['items']:
        print("TAKE " + values.get('name'))
    for values in player.inventory:
        print("DROP " + values.get('name'))


def main():
    """Function will display the options the user has, it will then read
    their input and go on to to the parser where their input will be
    corrected for the exe commands to work correctly"""
    # display the menu to the player
    print_menu()

    # take the user input
    user_input = input('>')

    # normal the input
    normal_user_input = normal_input(user_input)

    return normal_user_input
