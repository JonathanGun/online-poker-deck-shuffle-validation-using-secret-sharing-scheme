import random
from decimal import Decimal

import numpy as np
from pipe import where
from primePy import primes

SEED_MAX = int(1e5)
X_MAX = int(1e2)
PRIMES = primes.upto(SEED_MAX)
NUM_CARDS = 52


class Poker:
    def __init__(self, n_player=4):
        self.N = n_player

    def generate_seed(self, M=None, P=None, S=None):
        self.M = M
        self.P = P
        self.S = S
        if self.M is None:
            self.M = random.randint(0, SEED_MAX)
        if self.P is None:
            self.P = random.choice(list(PRIMES | where(lambda x: x > self.M and x > self.N)))
        if self.S is None:
            self.S = np.random.randint(0, SEED_MAX, self.N)
            self.S[0] = self.M

    def generate_share(self):
        self.s = np.polynomial.Polynomial(self.S)
        self.ys = []
        self.shares = []
        for _ in range(self.N):
            y = None
            while y is None or (y % NUM_CARDS) in self.ys:
                x = random.randint(0, X_MAX)
                y = int(self.s(x))
            self.ys.append(y)
            self.shares.append((x, y))

    def shuffle_deck(self, seed=None):
        if seed is None:
            seed = self.M
        self.deck = set(i for i in range(1, NUM_CARDS + 1))
        self.deck = list(self.deck - set(self.ys))
        random.Random(seed).shuffle(self.deck)
        return self.deck.copy()

    def deal_cards(self):
        self.player_cards = []
        for i in range(self.N):
            self.player_cards.append((self.ys[i] % NUM_CARDS, self.deck.pop(0)))
        return self.player_cards.copy()

    def open_community_cards(self):
        self.community_cards = []
        for _ in range(5):
            self.community_cards.append(self.deck.pop(0) % NUM_CARDS)
        return self.community_cards.copy()

    def combine_shares(self):
        sums = 0
        for j, share_j in enumerate(self.shares):
            xj, yj = share_j
            prod = Decimal(1)
            for i, share_i in enumerate(self.shares):
                xi, _ = share_i
                if i != j:
                    prod *= Decimal(Decimal(xi) / (xi - xj))
            prod *= Decimal(yj)
            sums += Decimal(prod)
        return int(round(Decimal(sums), 0))

    def __repr__(self):
        ret = [
            f"N={self.N}",
            f"M={self.M}",
            f"S[]={list(self.S[1:])}",
            f"s(x)={self.s}",
            f"x[]={list(map(lambda x: x[0], self.shares))}",
            f"y[]={list(map(lambda x: x[0], self.player_cards))}",
            f"z[]={list(map(lambda x: x[1], self.player_cards))}",
            f"t[]={self.community_cards}",
            "",
        ]
        return "\n".join(map(str, ret))


if __name__ == "__main__":
    poker = Poker(n_player=4)
    poker.generate_seed()
    poker.generate_share()
    poker.shuffle_deck()
    poker.deal_cards()
    poker.open_community_cards()
    print(poker)
