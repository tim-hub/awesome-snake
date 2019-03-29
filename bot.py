from functools import reduce
import pprint

pp = pprint.PrettyPrinter(indent=2)


def make_a_decision(board, you):
    # analyze the map and bot
    height = board.get('height', 0)
    width = board.get('width', 0)
    snakes = board.get('snakes', [])
    all_body_list = [b.get('body', []) for b in snakes]
    all_bodies = list(reduce(lambda x, y: x + y, all_body_list))
    food = board.get('food', [])

    the_map, the_map_dict = get_map(height, width, all_bodies, food)

    you_body = you.get('body', [])
    you_head = you_body[0]
    print(the_map_dict)
    return survive(you_head, the_map_dict)


def get_map(height, width, all_bodies, food, heads=[]):
    the_map = []
    the_map_dict = {}
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
            the_map_dict[(tmp_pos.get('x'), tmp_pos.get('y'))] = flag
        the_map.append(the_row)
    pp.pprint(the_map)
    return the_map, the_map_dict


def survive(the_head, the_map_dict):
    x = the_head.get('x')
    y = the_head.get('y')
    arounds = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]

    directions = {}
    directions.setdefault((x, y - 1), 'up')
    directions.setdefault((x, y + 1), 'down')
    directions.setdefault((x - 1, y), 'left')
    directions.setdefault((x + 1, y), 'right')

    decisions = {}
    for around in arounds:
        decisions.setdefault(around, 0)
        flag = the_map_dict.get(around, False)
        if flag:
            if flag == 'f':
                decisions[around] = 1
            elif flag == 'b':
                decisions[around] = -1
            else:
                decisions[around] = 0
        else:
            decisions[around] = -100
    pp.pprint(decisions)
    decision = max(decisions.keys(), key=(lambda key: decisions[key]))
    print(decision)
    return {"move": directions[decision]}
