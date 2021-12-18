import unittest

from main import Poker


class NormalFlow(unittest.TestCase):
    def test_normal_4_player(self):
        N_TEST = 1
        n_player = 4
        for _ in range(N_TEST):
            poker = Poker(n_player=n_player)
            poker.generate_seed()
            poker.generate_share()
            deck_before = poker.shuffle_deck()
            poker.deal_cards()
            poker.open_community_cards()
            print(poker)

            # verify
            poker_verify = Poker(n_player=n_player)
            poker_verify.generate_seed(poker.combine_shares(), poker.P, poker.S)
            poker_verify.generate_share()
            deck_after = poker_verify.shuffle_deck()
            poker_verify.deal_cards()
            poker_verify.open_community_cards()
            print(poker_verify)

            # assert
            assert poker.M == poker_verify.M
            identical = True
            for i in range(n_player + 5):
                if deck_before[i] != deck_after[i]:
                    identical = False
            assert identical

    def test_normal_6_player(self):
        N_TEST = 1
        n_player = 6
        for _ in range(N_TEST):
            poker = Poker(n_player=n_player)
            poker.generate_seed()
            poker.generate_share()
            deck_before = poker.shuffle_deck()
            poker.deal_cards()
            poker.open_community_cards()
            print(poker)

            # verify
            poker_verify = Poker(n_player=n_player)
            poker_verify.generate_seed(poker.combine_shares(), poker.P, poker.S)
            poker_verify.generate_share()
            deck_after = poker_verify.shuffle_deck()
            poker_verify.deal_cards()
            poker_verify.open_community_cards()
            print(poker_verify)

            # assert
            assert poker.M == poker_verify.M
            identical = True
            for i in range(n_player + 5):
                if deck_before[i] != deck_after[i]:
                    identical = False
            assert identical

    def test_alter_deck_after_shuffle(self):
        N_TEST = 1
        n_player = 4
        for _ in range(N_TEST):
            poker = Poker(n_player=n_player)
            poker.generate_seed()
            poker.generate_share()
            deck_before = poker.shuffle_deck()
            # alter deck
            for i in range(5):
                poker.deck[i * 2 + n_player], poker.deck[i * 2 + 1 + n_player] = poker.deck[i * 2 + 1 + n_player], poker.deck[i * 2 + n_player]
                deck_before[i * 2 + n_player], deck_before[i * 2 + 1 + n_player] = deck_before[i * 2 + 1 + n_player], deck_before[i * 2 + n_player]
            poker.deal_cards()
            poker.open_community_cards()
            print(poker)

            # verify
            poker_verify = Poker(n_player=n_player)
            poker_verify.generate_seed(poker.combine_shares(), poker.P, poker.S)
            poker_verify.generate_share()
            deck_after = poker_verify.shuffle_deck()
            poker_verify.deal_cards()
            poker_verify.open_community_cards()
            print(poker_verify)

            # assert
            assert poker.M == poker_verify.M
            identical = True
            for i in range(n_player + 5):
                if deck_before[i] != deck_after[i]:
                    identical = False
            assert not identical

    def test_change_seed(self):
        N_TEST = 1
        n_player = 4
        for _ in range(N_TEST):
            poker = Poker(n_player=n_player)
            poker.generate_seed()
            poker.generate_share()
            # change secret
            poker.M += 1
            deck_before = poker.shuffle_deck()
            poker.deal_cards()
            poker.open_community_cards()
            print(poker)

            # verify
            poker_verify = Poker(n_player=n_player)
            poker_verify.generate_seed(poker.combine_shares(), poker.P, poker.S)
            poker_verify.generate_share()
            deck_after = poker_verify.shuffle_deck()
            poker_verify.deal_cards()
            poker_verify.open_community_cards()
            print(poker_verify)

            # assert
            assert poker.M != poker_verify.M
            identical = True
            for i in range(n_player + 5):
                if deck_before[i] != deck_after[i]:
                    identical = False
            assert not identical


if __name__ == "__main__":
    unittest.main()
