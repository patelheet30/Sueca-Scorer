import sueca_suits_ranks as sr


class CardInvalid(Exception):
    def __init__(self, cs, emsg=""):
        str = "Card '{k}' is invalid!\n{m}"
        self.cs = cs
        self.msg = str.format(k = cs, m=emsg)
        super().__init__(self.msg)
        

class Card:
    """
    A class to represent a card.
    
    ...
    
    Attributes
    ----------
    card : str
        The card
    
    Methods
    -------
    points:
        The points the card is worth
    higher_than(other, s, t):
        Whether one card is higher than another compared to the lead suit and trump suit
    show:
        Shows the card in a string value
    
    """
    
    def __init__(self, card: str):
        """
        Constructs all the necessary attributes for the card object
        
            Parameters:
                card (str):
                    The card

        """
        self.card = card
        

    def points(self):
        """
        The points a card is worth
        
            Returns:
                points (int): The points a card is worth
        """
        return sr.rank_points(self.card)
    

    def higher_than(self, other: str, s: str, t: str):
        """
        Whether one card is higher than another

            Parameters:
                other (str): The compared which is used for comparison
                s (str): The lead suit
                t (str): The trump suit
            
            Returns:
                answer (bool): Returns whether the card is worth more than another

        """
        
        comparing_card = self.card
        comparing_card_points = sr.rank_points(comparing_card)
        
        test_card = other
        if isinstance(test_card, str):
            compared_card = test_card
            compared_card_points = sr.rank_points(test_card)
        else:
            compared_card = test_card.show()
            compared_card_points = sr.rank_points(test_card.show())
            
        lead_suit = s
        trump_suit = t

        
        
        """
        Old code which didn't properly factor in rank points and the ability for cards to have the same suits
        
        if comparing_card[1] == lead_suit and compared_card[1] != trump_suit and comparing_card_points > compared_card_points:
            return True
        elif comparing_card[1] == trump_suit and compared_card[1] != trump_suit and comparing_card_points > compared_card_points:
            return True
        elif comparing_card[1] == lead_suit and compared_card[1] != lead_suit and comparing_card_points > compared_card_points:
            return True
        else:
            return False
        """
        
        if sr.rank_higher_than("2D", "7D"):
            pass
        
        
        if comparing_card[-1] == compared_card[-1]:
            if comparing_card_points > compared_card_points:
                return True
            elif comparing_card == compared_card:
                return False
            elif comparing_card_points < compared_card_points:
                return False
            elif int(comparing_card[0]) > int(compared_card[0]):
                return True
            else:
                return False         
        else:
            if comparing_card[-1] == lead_suit and compared_card[-1] != trump_suit or comparing_card[-1] == trump_suit:
                return True
            else:
                return False


    def show(self):
        """
        Shows the card in str form
            Returns:
                answer (str): The string format of the instance of the card object

        """
        return self.card


def parseCard(cs: str):
    """
    Returns an instance of the Card object
    
        Parameters:
            cs (str): The card used
            
        Raises:
            CardInvalid: Raises an issue if the card is invalid
            
        Returns:
            new_card (Card): An object instance of class Card

    """
    if len(cs) > 2:
        raise CardInvalid(cs)
    elif cs[0] not in sr.ranks:
        raise CardInvalid(cs)
    elif cs[1] not in sr.suits:
        raise CardInvalid(cs)
    else:
        new_card = Card(cs)
        return new_card
