# -*-: coding utf-8 -*-
""" Skeleton Snips skill. """

from peewee import *

db = SqliteDatabase('people.db')

class Game(Model):
    winner = CharField()
    loser = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    score = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.


class PingPongSkill:
    """ Skeleton Snips skill. """

    def __init__(self):
	pass

    def hello_word(self):
        print "Coucou"

    def register_game(self, winner, loser, score):
        new_game = Game.create(winner, loser, score)


    def turn_on(self):
        """ Turn on something. """
        print("Turn on")


    def turn_off(self):
        """ Turn of something. """
        print("Turn off")


    def set_color_name(self, object_color):
        """ Set an object color. """
        print("Set object color to {}".format(object_color))
