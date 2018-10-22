# all room details are in this file
# room details have to be filled in
import items

room_main_door = {

    'door': False,

}

room_lobby = {
    'name': 'main lobby',

    'description': 'the main landing of the house',

    'items': [items.item_note1],

    'items_not': [],

    'exits': {'west': 'kitchen', 'east': 'bathroom', 'up': 'stairs', 'south': 'main door'},

    'door': True,

}

room_kitchen = {
    'name': 'kitchen',

    'description': 'A kitchen and a dinning room',

    'items': [items.item_riddle_clock, items.item_pendulum],

    'items_not': [],

    'exits': {'east': 'lobby',},

    'door': True,

}

room_bathroom = {
    'name': 'bathroom',

    'description': '',

    'items': [items.item_paper, items.item_building_block],

    'items_not': [items.item_bath, items.item_sink, items.item_toilet, items.item_cabinet, 
    items.item_mirror],

    'exits': {'west': 'lobby'},

    'door': True,

}

room_nursery = {
    'name': 'nursery',

    'description': '',

    'items': [],

    'items_not': [],

    'exits': {'east': 'landing floor', },

    'door': False,

}

room_bedroom = {
    'name': 'bedroom',

    'description': '',

    'items': [items.item_riddle_candle,
              items.item_matchsticks,],

    'items_not': [],

    'exits': {'west': 'landing floor', },

    'door': True,

}

room_stairs = {
    'name': 'stairs',

    'description': '',

    'items': [],

    'items_not': [],

    'exits': {'down': 'lobby', 'up': 'landing floor', },

    'door': True,

}

room_landing_floor_1 = {
    'name': 'landing floor',

    'description': '',

    'items': [],

    'items_not': [items.item_photo_frame],

    'exits': {'west': 'nursery', 'east': 'bedroom', 'down': 'stairs' },

    'door': True,

}



rooms_id = {
    'lobby': room_lobby,
    'kitchen': room_kitchen,
    'bathroom': room_bathroom,
    'nursery': room_nursery,
    'bedroom': room_bedroom,
    'stairs': room_stairs,
    'landing floor': room_landing_floor_1,
    'main door': room_main_door

}
