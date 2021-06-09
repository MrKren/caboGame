import random


class Card(object):

    def __init__(self, num=None, suit=None, known=True):

        self.known = known

        if num is None or suit is None:
            self.num = random.randint(1, 13)
            self.suit = random.randint(1, 4)
        else:
            self.num = num
            self.suit = suit

    def __repr__(self):

        if self.known:
            nums = {1: "A", 11: "J", 12: "Q", 13: "K"}
            for i in range(2, 11):
                nums[i] = str(i)
            suits = {1: u'\u2660', 2: u'\u2665', 3: u'\u2666', 4: u'\u2663'}

            return f"{nums[self.num]}{suits[self.suit]}"

        return f"##"


class Hand(object):

    def __init__(self, card_num: int):

        self.cards = [Card() for _ in range(card_num)]
        for card in self.cards[:len(self.cards)//2]:
            card.known = False

    def __len__(self):

        return len(self.cards)

    def state(self):
        rows = []
        row = ""
        for i, card in enumerate(self.cards):
            if i % 3 == 0:
                rows.append(row)
                row = ""
            row += f"({i+1}) {card}    "
        rows.append(row)

        for i in rows[1:]:
            print(i)
        print(f"Score: {self.score()}")

    def score(self):
        score = 0
        for card in self.cards:
            if card.known:
                if (card.num == 13) and (card.suit == 2 or card.suit == 3):
                    score -= 1  # Red Kings are worth -1
                else:
                    score += card.num

        return score

    def replace(self, card: Card, pos: int):
        self.cards[pos-1] = card


class GameRules(object):

    def __init__(self, players: int):
        self.hands = [Hand(6) for _ in range(players)]
        self.turn_num = 1
        self.final_turn = 0
        self.final_player = None
        self.stack = [Card()]
        self.stack_card = None
        self.hand = None

    def turn(self):
        print(f"Turn : {self.turn_num}\n")
        for i, self.hand in enumerate(self.hands):

            if self.hand == self.final_player:
                break

            print(f"Player {i + 1}")
            self.hand.state()
            self.stack_card = self.stack.pop()
            print(f"Stack : {self.stack_card}")

            if input("Replace (y/n):\n").lower() == "y":
                self.replace()
            else:
                self.stack.append(Card())
                self.stack_card = self.stack.pop()
                print(f"Top Deck : {self.stack_card}")
                key_word = input("Choices: play, swap\n")
                if key_word == "swap":
                    self.replace()
                else:
                    self.play()
            if self.final_turn == 0:
                if input("Cabo ?\n").lower() == "y":
                    self.final_turn = self.turn_num + 1
                    self.final_player = self.hand

        self.turn_num += 1

    def winner(self):
        self.turn()
        print(f"Final Scores:\n")
        for i, hand in enumerate(self.hands):
            for card in hand.cards:
                card.known = True
            print(f"Player {i+1}: {hand.score()}")
        print("\n")
        for hand in self.hands:
            hand.state()

    def play(self):
        self.stack.append(self.stack_card)

    def replace(self):
        pos = int(input(f"Position (1-{len(self.hand)}): "))
        self.hand.cards[pos-1].known = True
        self.stack.append(self.hand.cards[pos-1])
        self.hand.cards[pos-1] = self.stack_card


game = GameRules(3)

# Game Loop
while game.turn_num != game.final_turn:
    game.turn()
game.winner()
