import random


class Card(object):

    def __init__(self, num: int, suit: int):
        self.num = num
        self.suit = suit
        pass

    def __repr__(self):
        pass

    def flip(self):
        pass


class Hand(object):

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def add_card(self):
        pass

    def remove_card(self):
        pass


class Pile(Hand):

    def __repr__(self):
        pass


class Turn(object):

    def __init__(self):
        pass


class Table(object):

    def __init__(self):
        pass


class Action(object):

    def __init__(self):
        pass

    def perform(self):
        pass


class BlindSwap(Action):

    def perform(self):
        pass


class LookSwap(Action):

    def perform(self):
        pass


class PeekOwn(Action):

    def perform(self):
        pass


class PeekOther(Action):

    def perform(self):
        pass


class SwipePile(Action):

    def perform(self):
        pass
