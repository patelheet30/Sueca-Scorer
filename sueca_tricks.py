import sueca_cards as sc
import sueca_suits_ranks as sr

def parseTrick(ts):
    ts_split = ts.split(" ")
    if len(ts_split) != 4:
        raise ValueError(f"A trick string must comprise four cards only; the given trick is: {ts}")
    else:
        for card in ts_split:
            sc.parseCard(card)
    
    new_trick = Trick(ts)
    return new_trick

def parseGameFile(fname):
    file_opened = fname
    game = open(file_opened, 'r')
    entire_game = []
    for line in game:
        new_line = line.rstrip()
        entire_game.append(new_line)
    parsed_trump = sc.parseCard(entire_game[0])
    parsed_game = entire_game[1:]
    complete_game = []
    for parsed_game_line in parsed_game:
        complete_game.append(parseTrick(parsed_game_line))
    return (parsed_trump, complete_game)
        

class Trick:
    
    def __init__(self, trick):
        self.trick = trick
    
    def show(self):
        return self.trick
    
    def points(self):
        trick = self.trick
        trick_split = trick.split(" ")
        points = 0
        for card in trick_split:
            points += sr.rank_points(card)
        
        test_passer = sc.Card("AD")
        test_points = test_passer.points()
        
        
        return points
    
    def trick_winner(self, t):
        each_card = self.trick.split(" ")
        collected_cards = []
        
        for card in each_card:
            if card[-1] == t:
                collected_cards.append(card)
            else:
                continue
        if len(collected_cards) > 1:
            highest_rank = collected_cards[0]
            highest_rank_card = sc.Card(highest_rank)
            
            
        lead_suit = each_card[0][-1]
        highest_rank_in_each_card = each_card[0]
        highest_rank_in_each_card = sc.Card(highest_rank_in_each_card)
        
        if len(collected_cards) == 1:
            return each_card.index(collected_cards[0]) + 1
        elif len(collected_cards) > 1:
            for collected_card in collected_cards:
                
                if sc.parseCard(collected_card).higher_than(highest_rank_card, lead_suit, t) == True:
                    highest_rank_card = collected_card
                else:
                    continue
            if isinstance(highest_rank_card, str):
                return each_card.index(highest_rank_card) + 1
            else:
                return each_card.index(highest_rank_card.show()) + 1
        else:
            for card in each_card:
                if sc.parseCard(card).higher_than(highest_rank_in_each_card, lead_suit, t) == True:
                    highest_rank_in_each_card = card
                else:
                    continue
            if isinstance(highest_rank_in_each_card, str):
                return each_card.index(highest_rank_in_each_card) + 1
            else:
                return each_card.index(highest_rank_in_each_card.show()) + 1
            

