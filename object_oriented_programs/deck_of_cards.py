"""
Overview:
This is the method which contains DeckOfCards.
Purpose:
Shuffle the cards using Random method and then distribute 9 Cards to 4 Players and
Print the Cards the received by the 4 Players using 2D Array.
Author: Rutuja Tikhile
Date: 29/01/2020
"""
import random


class DeckOfCards:
    def __init__(self):
        """
        Creating five dictionary which having four keys ("Clubs", "Diamonds", "Hearts", "Spades")
        and values and three tuples(suit, rank, players).
        """
        self.card = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.suit = ("Clubs", "Diamonds", "Hearts", "Spades")
        self.rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        self.player1 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.player2 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.player3 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.player4 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.players = (self.player1, self.player2, self.player3, self.player4)

    def deck_of_cards(self):
        """
        Shuffle all the cards, like shuffle the cards using Random method and then distribute 9 Cards to 4 Players.
        i.e total count = 9*4(36).
        :return: 9 Distinct cards.
        """
        count = 36
        while count > 0:
            random_suit = self.suit[random.randrange(0, 4)]
            random_rank = self.rank[random.randrange(0, 13)]
            temp = self.card[random_suit]
            flag = True
            for i in range(len(temp)):
                if temp[i] == random_rank:
                    flag = False
                    break
            if flag:
                self.card[random_suit].append([random_rank])
                count -= 1

    def deck_card_assign(self):
        """
        Assign 9 deck of card to each player.
        :return:players having distinct cards.
        """
        count = 0
        for i in self.suit:
            temp = self.card[i]
            for j in range(len(temp)):
                if count >= 4:
                    count = 0
                self.players[count][i].append(temp[j])
                count += 1

    def card_display(self):
        """
        Display cards.
        :return:
        """
        for i in range(len(self.players)):
            print("players", i+1)
            print("Clubs: ", self.players[i]["Clubs"])
            print("Diamonds: ", self.players[i]["Diamonds"])
            print("Hearts: ", self.players[i]["Hearts"])
            print("Spades: ", self.players[i]["Spades"])
            print()


if __name__ == "__main__":
    DeckOfCards()
    obj = DeckOfCards()
    obj.deck_of_cards()
    obj.deck_card_assign()
    obj.card_display()