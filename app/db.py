import os
import psycopg2

# store all game turn information for further data processing for build machine learning models

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')



def init_db(init_data):
    cur = conn.cursor()

    QUERY_CREATE_GAME = '''
        CREATE TABLE IF NOT EXISTS games (
        id SERIAL PRIMARY KEY,
        game_id INTEGER NOT NULL,
        game_info json NOT NULL);
        '''

    QUERY_CREATE_TURN = '''
        CREATE TABLE IF NOT EXISTS turns(
        id SERIAL PRIMARY KEY,
        turn INTEGER NOT NULL,
        turn_info json NOT NULL,
        game_id INTEGER NOT NULL
        );
        '''

    # CREATE INDEX game_id_index ON games(game_id );
    # CREATE INDEX turn_indexes on turns(turn,game_id);
    cur.execute(QUERY_CREATE_GAME)
    cur.execute(QUERY_CREATE_TURN)
    insert_game(cur, init_data)
    return cur

def insert_game(cur, init_data):
    game_id = init_data.get("game").get("id", -1)
    game_info = init_data
    query = '''
    INSERT INTO games (game_id, game_info)
    VALLUES(%s, %s);
    '''
    cur.execute(query, (game_id, game_info))


def insert_turn(cur, data):
    game_id = data.get("game").get("id", -1)
    turn_id = data.get("turn")
    turn_info = data
    query = '''
    INSERT INTO turns (turn_id, turn_info, game_id)
    VALLUES(%s, %s, %s);
    '''
    cur.execute(query, (turn_id, turn_info, game_id))

def close_db(cur):
    conn.commit()
    cur.close()
    conn.close()