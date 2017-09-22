# -*-: coding utf-8 -*-
""" Skeleton Snips skill. """

from peewee import *
import datetime
import json



class PingPongSkill:
    """ Skeleton Snips skill. """

    def __init__(self):
        pass

    def load(self):
        pass

    def save(self):
        pass

    def handle_terminate_game(self, intent):
        print "*** {}".format(intent)
        with open('/home/pi/intent.json', 'w') as f:
            json.dump(intent, f)
