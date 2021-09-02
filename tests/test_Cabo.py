from unittest import TestCase
from game.Cabo import *


class TestCard(TestCase):
    def test_flip_up(self):
        card = Card(1, 1, False)
        self.assertEqual(str(card), "##")
        card.flip_up()
        self.assertEqual(str(card), "A" + u'\u2660')
        card.flip_up()
        self.assertEqual(str(card), "A" + u'\u2660')

    def test_flip_down(self):
        card = Card(1, 1, True)
        self.assertEqual(str(card), "A" + u'\u2660')
        card.flip_down()
        self.assertEqual(str(card), "##")
        card.flip_down()
        self.assertEqual(str(card), "##")

    def test_peek(self):
        card = Card(1, 1, True)
        self.assertEqual(card.peek(), "A" + u'\u2660')
        card = Card(1, 1, False)
        self.assertEqual(card.peek(), "A" + u'\u2660')
        self.assertEqual(str(card), "##")


class TestHand(TestCase):
    def test_add_card(self):
        hand = Hand(6)
        card = RandomCard(True)
        self.assertEqual(len(hand), 6)
        hand.add_card(card)
        self.assertEqual(len(hand), 7)
        self.assertEqual(hand.cards[-1], card)

    def test_remove_card(self):
        hand = Hand(6)
        card = hand.cards[0]
        cards = hand.cards[1:]
        self.assertEqual(len(hand), 6)
        hand.remove_card(card)
        self.assertEqual(len(hand), 5)
        self.assertEqual(hand.cards, cards)


class TestTurn(TestCase):
    def test_actions(self):
        self.fail()


class TestTable(TestCase):
    def test_update(self):
        self.fail()


class TestBlindSwap(TestCase):
    def test_perform(self):
        self.fail()


class TestLookSwap(TestCase):
    def test_perform(self):
        self.fail()


class TestPeekOwn(TestCase):
    def test_perform(self):
        self.fail()


class TestPeekOther(TestCase):
    def test_perform(self):
        self.fail()


class TestSwipePile(TestCase):
    def test_perform(self):
        self.fail()


if __name__ == '__main__':
    import unittest

    unittest.main()