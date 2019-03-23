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
    return Response({'Server is running.'}, status=200, mimetype='application/json')

@app.route('/start')
def start():
    return Response({'Starting the game.'}, status=200, mimetype='application/json')


@app.route('/move')
def move():
    logging.info(request.data)
    return Response(
        {
            "move": "left"
        },
        status=200,
        mimetype='application/json')


@app.route('/end')
def end():
    return Response({'Ending the game.'}, status=200, mimetype='application/json')


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