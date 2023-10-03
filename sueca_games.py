import sueca_cards as sc
import sueca_tricks as st

class CardAlreadyPlayed(Exception):
    pass
class DealerDoesNotHoldTrumpCard(Exception):
    pass
class IllegalCardPlayed(Exception):
    pass

class Game:

    def __init__(self, game):
        self.game = game
        self.score1 = 0
        self.score2 = 0
        self.player1pos = 1
        self.player2pos = 2
        self.player3pos = 3
        self.player4pos = 4
        self.player1card = []
        self.player2card = []
        self.player3card = []
        self.player4card = []
        self.player1pcard = []
        self.player2pcard = []
        self.player3pcard = []
        self.player4pcard = []
        self.duplicate_card_tracker = []
        self.tricks = []
        
        
    def gameTrump(self):
        card = self.game.show()
        return sc.Card(card)
    

    def score(self):
        return (self.score1, self.score2)
    
    
    def playTrick(self, t):
        trick_str = t.show()
        trick_obj = st.Trick(trick_str)
        playedTrick = trick_obj.trick_winner(self.game.show()[-1])
        self.tricks.append(trick_obj)
        
        
        if playedTrick == self.player1pos:
            cards_in_trick = trick_str.split(" ")
            self.player1card.append(cards_in_trick[self.player1pos - 1])
            self.player2card.append(cards_in_trick[self.player2pos - 1])
            self.player3card.append(cards_in_trick[self.player3pos - 1])
            self.player4card.append(cards_in_trick[self.player4pos - 1])
            self.player1pos = 1
            self.player2pos = 2
            self.player3pos = 3
            self.player4pos = 4
            self.score1 += trick_obj.points()
        
        elif playedTrick == self.player2pos:
            cards_in_trick = trick_str.split(" ")
            self.player1card.append(cards_in_trick[self.player1pos - 1])
            self.player2card.append(cards_in_trick[self.player2pos - 1])
            self.player3card.append(cards_in_trick[self.player3pos - 1])
            self.player4card.append(cards_in_trick[self.player4pos - 1])
            self.player1pos = 4
            self.player2pos = 1
            self.player3pos = 2
            self.player4pos = 3
            self.score2 += trick_obj.points()
        
        elif playedTrick == self.player3pos:
            cards_in_trick = trick_str.split(" ")
            self.player1card.append(cards_in_trick[self.player1pos - 1])
            self.player2card.append(cards_in_trick[self.player2pos - 1])
            self.player3card.append(cards_in_trick[self.player3pos - 1])
            self.player4card.append(cards_in_trick[self.player4pos - 1])
            self.player1pos = 3
            self.player2pos = 4
            self.player3pos = 1
            self.player4pos = 2
            self.score1 += trick_obj.points()
        
        elif playedTrick == self.player4pos:
            cards_in_trick = trick_str.split(" ")
            self.player1card.append(cards_in_trick[self.player1pos - 1])
            self.player2card.append(cards_in_trick[self.player2pos - 1])
            self.player3card.append(cards_in_trick[self.player3pos - 1])
            self.player4card.append(cards_in_trick[self.player4pos - 1])
            self.player1pos = 2
            self.player2pos = 3
            self.player3pos = 4
            self.player4pos = 1
            self.score2 += trick_obj.points()
            
        if len(self.player4card) == 10:
            if self.game.show() not in self.player2card:
                raise DealerDoesNotHoldTrumpCard(f"Player 2 (dealer) does not hold the trump card {self.game.show()}")
                
            for card in self.player1card:
                self.player1pcard.append(sc.Card(card))
                
            for card in self.player2card:
                self.player2pcard.append(sc.Card(card))
                
            for card in self.player3card:
                self.player3pcard.append(sc.Card(card))
                
            for card in self.player4card:
                self.player4pcard.append(sc.Card(card))
                
        tracker_helper = trick_str.split(" ")
        for card in tracker_helper:
            self.duplicate_card_tracker.append(card)
             
        if len(self.duplicate_card_tracker) != len(set(self.duplicate_card_tracker)):
            raise CardAlreadyPlayed("A duplicate card was played")
        
        

    def cardsOf(self, p):
        if p > 4:
            raise ValueError(f"Invalid player number: {p}")
        else:
            if p == 1:
                return self.player1pcard
            elif p == 2:
                return self.player2pcard
            elif p == 3:
                return self.player3pcard
            elif p == 4:
                return self.player4pcard
            
        
    def gameTricks(self):
        return self.tricks
        
            
            

        
