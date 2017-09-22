# -*-: coding utf-8 -*-
""" Skeleton Snips skill. """

from peewee import *
import datetime




class PingPongSkill:
    """ Skeleton Snips skill. """

    def __init__(self):
        pass

    def load(self):
        pass

    def save(self):
        pass

    def handle_terminate_game(self, intent):
        print "*** " + str(intent)
