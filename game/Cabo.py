import random


class Card(object):

    def __init__(self, num=None, suit=None, known=True):

        self.known = known
        self.nums = {1: "A", 11: "J", 12: "Q", 13: "K"}
        for i in range(2, 11):
            self.nums[i] = str(i)
        self.suits = {1: u'\u2660', 2: u'\u2665', 3: u'\u2666', 4: u'\u2663'}

        self.num = num
        self.suit = suit

        if num is None:
            self.num = random.randint(1, 13)
        if suit is None:
            self.suit = random.randint(1, 4)

    def __repr__(self):

        if self.known:
            return self.peek()

        return f"##"

    def peek(self):

        return f"{self.nums[self.num]}{self.suits[self.suit]}"

    def flip(self):

        self.known = True


class Hand(object):

    def __init__(self, card_num: int, index: int):

        self.cards = [Card() for _ in range(card_num)]
        self.index = index
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
        self.hands = [Hand(6, i+1) for i in range(players)]
        self.turn_num = 1
        self.final_turn = 0
        self.final_player = None
        self.stack = [Card()]
        self.stack_card = Card()
        self.hand = None

    def turn(self):
        print(f"Turn : {self.turn_num}\n")
        for self.hand in self.hands:

            if self.hand == self.final_player:
                break

            print(f"Player {self.hand.index}")
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
        for hand in self.hands:
            for card in hand.cards:
                card.known = True
            print(f"Player {hand.index}: {hand.score()}")
        print("\n")
        for hand in self.hands:
            hand.state()

    def play(self):
        self.stack.append(self.stack_card)
        if (self.stack_card.num == 7) or (self.stack_card.num == 8):
            self.peek()
        if (self.stack_card.num == 9) or (self.stack_card.num == 10):
            self.peek_other()
        if (self.stack_card.num == 11) or (self.stack_card.num == 12):
            self.swap()

    def get_players(self):
        player_choices = self.hands.copy()
        player_choices.remove(self.hand)

        return player_choices

    def swap(self):
        pos = int(input(f"Your position (1-{len(self.hand)}): "))

        player_choice = int(input(f"Pick a player to swap with ({[hand.index for hand in self.get_players()]}): "))
        player_choice = self.hands[player_choice-1]
        player_pos = int(input(f"Their position (1-{len(player_choice)}): "))

        place_holder = player_choice.cards[player_pos-1]
        player_choice.cards[player_pos-1] = self.hand.cards[pos-1]
        self.hand.cards[pos-1] = place_holder

    def peek(self):
        pos = int(input(f"Pick a card to flip (1-{len(self.hand)}): "))
        self.hand.cards[pos-1].known = True
        print(self.hand.cards[pos-1])

    def peek_other(self):
        player_choice = int(input(f"Pick a player to peek with ({[hand.index for hand in self.get_players()]}): "))
        player_choice = self.hands[player_choice - 1]
        player_pos = int(input(f"Pick a card position (1-{len(player_choice)}): "))
        print(player_choice.cards[player_pos-1].peek())

    def replace(self):
        pos = int(input(f"Position (1-{len(self.hand)}): "))
        self.hand.cards[pos-1].known = True
        self.stack.append(self.hand.cards[pos-1])
        self.hand.cards[pos-1] = self.stack_card


if __name__ == "__main__":
    game = GameRules(3)

    # Game Loop
    while game.turn_num != game.final_turn:
        game.turn()
    game.winner()
