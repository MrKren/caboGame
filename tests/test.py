import unittest

from game.Cabo import Card


class TestCard(unittest.TestCase):

    def test_known(self):
        result = str(Card(num=1, suit=1))

        self.assertEqual(result, u"A\u2660")

    def test_unknown(self):
        result = str(Card(num=1, suit=1, known=False))

        self.assertEqual(result, "##")


if __name__ == "__main__":
    unittest.main()
