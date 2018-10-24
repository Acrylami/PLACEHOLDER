# all room details are in this file
# room details have to be filled in
import items

room_main_door = {

    'name': 'main door',

    'description': 'The only exit. You have to get out.',

    'door': False,

    'opened': False,

}

room_lobby = {
    'name': 'main lobby',

    'description': 'The lobby of your home. The lights are bright and unforgiving, hurting your eyes. An ornate coatrack stands in one corner of the room, at the foot of a winding staircase. A photo is mounted on the wall. ',

    'items': [],

    'items_not': [],

    'exits': {'west': 'kitchen', 'east': 'bathroom', 'up': 'stairs', 'south': 'main door'},

    'door': True,

}

room_kitchen = {
    'name': 'kitchen',

    'description': 'The room is spacious yet cluttered, dirty plates sit on the kitchen counter, pots and pans hang above the stove and an array of empty bottles litter the floor and worktop. You drank too much last night. There is an oven, fridge and a sink here.',

    'items': [items.item_riddle_clock, ],

    'items_not': [items.item_oven, items.item_fridge,],

    'exits': {'east': 'lobby',},

    'door': False,

}

room_bathroom = {
    'name': 'bathroom',

    'description': 'An ornate bath is the centrepiece of this room, made of marble. The toilet and sink sit towards the right of the room. The basin of the sink has a faint pink tinge, and the floor is damp as though recently cleaned. Above the sink is a cabinet. The smell of bleach is thick in this room..',

    'items': [items.item_paper,],

    'items_not': [items.item_bath, items.item_sink, items.item_toilet, items.item_cabinet,
    items.item_mirror],

    'exits': {'west': 'lobby'},

    'door': False,

}

room_nursery = {
    'name': 'nursery',

    'description': 'The walls of this room are covered in a galaxy print, with a small cot in the corner of the room. Toys take up most of the floor space. You feel uncomfortable here.',

    'items': [items.item_building_block, items.item_light_switch,],

    'items_not': [items.item_rack, items.item_cot,],

    'exits': {'east': 'landing floor', },

    'door': False,

}

room_bedroom = {
    'name': 'bedroom',

    'description': 'You open the door to the bedroom. A four poster canopy bed sits in the middle of the room with clothes strewn over it haphazardly. A wooden wardrobe stands to your left, open. To your right is a desk and a vanity. ',

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
