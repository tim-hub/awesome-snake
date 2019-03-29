from functools import reduce
import pprint

pp = pprint.PrettyPrinter(indent=2)

def get_map(board, you):
    # analyze the map and bot
    height = board.get('height', 0)
    width = board.get('width', 0)

    snakes = board.get('snakes', [])
    all_body_list = [b.get('body', []) for b in snakes]
    all_bodies = list(reduce(lambda x, y: x + y, all_body_list))
    food = board.get('food', [])

    you_body = you.get('body', [])
    you_head = you_body[0]

    the_map = []
    for i in range(height):
        the_row = []
        for j in range(width):
            flag = ' '
            tmp_pos = {
                'x': j,
                'y': i
            }
            if tmp_pos in all_bodies:
                flag = 'b'
            elif tmp_pos in food:
                flag = 'f'
            the_row.append(flag)
        the_map.append(the_row)
    pp.pprint(the_map)
    return the_map