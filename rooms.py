# all room details are in this file
# room details have to be filled in
import items

room_main_door = {

    'name': 'main door',

    'description': 'The only exit out of this mansion',

    'door': False,

    'opened': False,

}

room_lobby = {
    'name': 'main lobby',

    'description': 'the main landing of the house',

    'items': [],

    'items_not': [],

    'exits': {'west': 'kitchen', 'east': 'bathroom', 'up': 'stairs', 'south': 'main door'},

    'door': True,

}

room_kitchen = {
    'name': 'kitchen',

    'description': 'A kitchen and a dinning room',

    'items': [items.item_riddle_clock, ],

    'items_not': [items.item_oven, items.item_fridge,],

    'exits': {'east': 'lobby',},

    'door': False,

}

room_bathroom = {
    'name': 'bathroom',

    'description': '',

    'items': [items.item_paper,],

    'items_not': [items.item_bath, items.item_sink, items.item_toilet, items.item_cabinet,
    items.item_mirror],

    'exits': {'west': 'lobby'},

    'door': True,

}

room_nursery = {
    'name': 'nursery',

    'description': '',

    'items': [items.item_building_block, items.item_light_switch,],

    'items_not': [items.item_rack, items.item_cot,],

    'exits': {'east': 'landing floor', },

    'door': False,

}

room_bedroom = {
    'name': 'bedroom',

    'description': '',

    'items': [items.item_riddle_candle,
              items.item_matchsticks,
              items.item_pendulum],

    'items_not': [items.item_wardrobe, items.item_desk, items.item_bed, items.item_picture,],

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
