from app import db # db
from app import ma # serializer
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime


class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    game_uuid = db.Column(db.String, nullable=False, unique=True)
    game_info = db.Column(JSONB, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    turns = db.relationship('Turn', backref='game', lazy=True)
    def __repr__(self):
        return '<Game {} - {}>'.format(self.id, self.game_uuid)


class Turn(db.Model):
    __tablename__ = 'turn'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    turn_uuid = db.Column(db.String, nullable=False, unique=True)
    turn_info = db.Column(JSONB, nullable=False)
    def __repr__(self):
        return '<Turn of Game {},  {} - {}>'.format(self.game_id, self.id, self.turn_uuid)


class GameSchema(ma.Schema):
    class Meta:
        fields = ('game_uuid', 'game_info', 'created')

class TurnSchema(ma.Schema):
    class Meta:
        fields = ('game_id', 'turn_info', 'turn_uuid')
