import uuid
from flask import request, Response
from app import app, db, logging
from models import Game, Turn, GameSchema, TurnSchema

@app.route('/', methods=['POST', 'GET'])
def index():
    return '''
    Snake bot is OK, can got to fight now. This is the dev version.
    '''

@app.route('/ping', methods=['POST', 'GET'])
def ping():
    return {'message': 'Server is running.'}

@app.route('/start', methods=['POST', 'GET'])
def start():
    return {'message': 'Starting the game.'}


@app.route('/move', methods=['POST', 'GET'])
def move():
    logging.info(request.data)
    return  { "move": "left" }



@app.route('/end', methods=['POST', 'GET'])
def end():
    return {'message':'Ending the game.'}


@app.route('/admin')
def admin():
    # query results
    games = Game.query.all()
    turns = Turn.query.all()
    return {
        'message': 'all data for admin only',
        'data': {
            'games': GameSchema(many=True).dump(games)[0],
            'scans': TurnSchema(many=True).dump(turns)[0]
        }
    }