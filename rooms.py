# all room details are in this file
# room details have to be filled in
import items


room_lobby = {
    'name': 'main lobby',

    'description': 'the main landing of the house',

    'items': [items.item_note1],

    'exits': {'west': 'kitchen', 'east': 'bathroom', 'up': 'stairs'},

}

room_kitchen = {
    'name': 'kitchen',

    'description': '',

    'items': [],

    'exits': {'east': 'lobby', },

}

room_bathroom = {
    'name': 'bathroom',

    'description': '',

    'items': [],

    'exits': {'west': 'lobby'},

}

room_nursery = {
    'name': 'nursery',

    'description': '',

    'items': [],

    'exits': {'east': 'landing floor', },

}

room_bedroom = {
    'name': 'bedroom',

    'description': '',

    'items': [items.item_riddle_candle,
              items.item_matchsticks,
              ],

    'exits': {'west': 'landing floor', },


}

room_stairs = {
    'name': 'stairs',

    'description': '',

    'items': [],

    'exits': {'down': 'lobby', 'up': 'landing floor', },

}

room_landing_floor_1 = {
    'name': 'landing floor',

    'description': '',

    'items': [],

    'exits': {'west': 'nursery', 'east': 'bedroom', 'down': 'stairs' },

}


rooms_id = {
    'lobby': room_lobby,
    'kitchen': room_kitchen,
    'bathroom': room_bathroom,
    'nursery': room_nursery,
    'bedroom': room_bedroom,
    'stairs': room_stairs,
    'landing floor': room_landing_floor_1,

}
