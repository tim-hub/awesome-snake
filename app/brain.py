



def process_data(data):
    data = dict(data)

    board = data.get('board')
    height = board.get('height')
    width = board.get('width')
    foods = board.get('food')
    snakes = board.get('snakes')

    you = data.get("you")
    the_head = you.get('body')[0]
    around = [
        [the_head['x'] + 1, the_head['y']],
        [the_head['x'] - 1, the_head['y']],
        [the_head['x'], the_head['y'] + 1],
        [the_head['x'], the_head['y'] - 1],
    ]

    game_map = []
    for i in range(width):
        column = []
        for j in range(height):
            column.append(0)
            game_map.append(column)


    for food in foods:
        game_map[food['x']][food['y']] = 1

    for snake in snakes:
        for b in snake.get('body', []):
            game_map[b['x']][b['y']] = -1


    print(game_map)
    for i in range(width):
        for j in range(height):
            if [i, j] in around and game_map[i][j] >=0:
                if i > the_head['x']:
                    return 'right'
                elif i< the_head['x']:
                    return 'left'
                elif j< the_head['y']:
                    return 'down'
                else:
                    return 'up'

    return 'up'
