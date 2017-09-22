# -*-: coding utf-8 -*-
""" Skeleton Snips skill. """

import re
import json
import os
import datetime
from text2num import text2num
from collections import defaultdict

FORMAT = '%Y.%m.%dT%H:%M:%S'


class PingPongSkill(object):
    """ Skeleton Snips skill. """

    def __init__(self):
        pass

    def handle_loser(self):
        db = JsonDB()
        perfs = db.compute_perfs()
        if len(perfs) == 0:
            print "No match registred"
            return
        loser = sorted(perfs.iteritems(), key=lambda x: x[1])[0][0]
        print "The one who lost the most matches is {}".format(loser)

    def handle_winner(self):
        db = JsonDB()
        perfs = db.compute_perfs()
        if len(perfs) == 0:
            print "No match registred"
            return
        loser = sorted(perfs.iteritems(), key=lambda x: -x[1])[0][0]
        print "The one who lost the most matches is {}".format(loser)

    def handle_terminate_game(self, winner, loser, score):
        print "*** {} {} {}".format(winner, loser, score)
        try:
            score = parse_core(score)
        except ValueError, err:
            print err
        db = JsonDB()
        timestamp = datetime.datetime.now().strftime(FORMAT)
        db.add(winner, loser, score[0], score[1], timestamp)
        print "I added the match {} versus {}: score: {}".format(winner,
                                                                 loser,
                                                                 score)


regex = re.compile('([\w\s]+)to([\w\s]+)')


def parse_core(score):
    match = regex.search(score)
    if not match or len(match.groups()) != 2:
        raise ValueError("{} is an incorrect score".format(score))
    score_1 = text2num(match.groups()[0].strip())
    score_2 = text2num(match.groups()[1].strip())
    if score_1 != 11 and score_2 != 11:
        raise ValueError(
            "{} is an incorrect score: one of the player needs to have "
            "11".format(
                score))
    return sorted([score_1, score_2], reverse=True)


class JsonDB(object):
    path = 'ping_pong_db.json'

    def __init__(self):
        if not os.path.exists(self.path):
            self._results = []
        else:
            with open(self.path, 'r') as f:
                results = json.load(f)
            self._results = results

    def add(self, player_1, player_2, score_player_1, score_player_2,
            datetime_str):
        self._results += [
            (datetime_str, player_1, player_2, score_player_1, score_player_2)]
        self.save_results()

    def save_results(self):
        with open(self.path, 'w') as f:
            json.dump(self._results, f)

    def compute_perfs(self):
        player_to_win = defaultdict(int)
        player_to_lose = defaultdict(int)
        for _, win, lose, _, _ in self._results:
            player_to_win[win] += 1
            player_to_lose[lose] += 1
        player_to_proportion = {}
        for player in set(player_to_win.keys() + player_to_lose.keys()):
            proportion = float(player_to_win[player]) / (
                player_to_win[player] + player_to_lose[player])
            player_to_proportion[player] = proportion
        return player_to_proportion


if __name__ == '__main__':
    scores = [
        'eleven to two',
        'twenty to eleven'
    ]
    for score in scores:
        print parse_core(score)

    PingPongSkill().handle_loser()
    PingPongSkill().handle_terminate_game('thib', 'alex', 'eleven to two')
    PingPongSkill().handle_loser()

