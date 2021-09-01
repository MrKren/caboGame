import random


class Card(object):

    def __init__(self, num: int, suit: int, face_up: bool):
        self.num = num
        self.suit = suit
        self.face_up = face_up
        pass

    def __repr__(self):
        pass

    def flip_up(self):
        self.face_up = True

    def flip_down(self):
        self.face_up = False

    def peek(self) -> str:
        pass


class RandomCard(Card):

    def __init__(self, face_up: bool):
        num = random.randint(1, 13)
        suit = random.randint(1, 4)
        super().__init__(num, suit, face_up)


class Hand(object):

    def __init__(self, size: int):
        self.cards = []

    def __repr__(self):
        pass

    def __len__(self):
        return len(self.cards)

    def add_card(self):
        pass

    def remove_card(self):
        pass


class Pile(object):

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def take_card(self):
        pass

    def add_card(self):
        pass


class Turn(object):

    def __init__(self):
        pass

    def actions(self):
        pass


class Table(object):

    def __init__(self):
        pass

    def update(self):
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
