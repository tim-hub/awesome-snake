import uuid
from flask import request, Response
from app import app, db, logging
from models import Game, Turn, GameSchema, TurnSchema

@app.route('/')
def index():
    return '''
    Snake bot is OK, can got to fight now. This is the dev version.
    '''

@app.route('/ping')
def ping():
    return {'message': 'Server is running.'}

@app.route('/start')
def start():
    return {'message': 'Starting the game.'}


@app.route('/move')
def move():
    logging.info(request.data)
    return  { "move": "left" }



@app.route('/end')
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