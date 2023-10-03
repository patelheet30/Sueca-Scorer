suits = {
    "S": "Spades",
    "D": "Diamonds",
    "H": "Hearts",
    "C": "Clubs",
}

ranks = {
    "A": ["Ace", 11, 1],
    "7": ["Seven", 10, 2],
    "K": ["King", 4, 3],
    "J": ["Jack", 3, 4],
    "Q": ["Queen", 2, 5],
    "6": ["Six", 0, 6],
    "5": ["Five", 0, 7],
    "4": ["Four", 0, 8],
    "3": ["Three", 0, 9],
    "2": ["Two", 0, 10],
}


def valid_suit(s: str):
    """
    Checks if the suit is valid or not
    
        Parameters:
            s (str): The identifier used to find the suit name
            
        Returns:
            answer (bool): Whether the rank is valid or not
    """
    if s not in suits:
        return False  # Convert to make this into a boolean
    else:
        return True   # Convert to make this into a boolean


def valid_rank(r: str):
    """
    Checks if the rank is valid or not
    
        Parameters:
            r (str): The identifier used to find the rank name
            
        Returns:
            answer (bool): Whether the rank is valid or not
    """
    if len(r) == 1:
        rank = r[0]
    elif len(r) == 2:
        rank = r[0]
    else:
        rank = r
    if rank not in ranks:
        return False  # Convert to make this into a boolean
    else:
        return True  # Convert to make this into a boolean


def suit_full_name(s: str):
    """
    Returns the full name of the suit
    
        Parameters:
            s (str): The identifier used to find the full suit name
            
        Returns:
            answer (str): What the suits full name is
    """
    suit = s[-1]

    if suit in suits:
        return suits[f'{suit}']
    else:
        raise ValueError(f"invalid suit symbol: {suit}")
    


def rank_points(r: str):
    """
    Returns the points associated with the given rank
    
        Parameters:
            r (str): A string which contains the rank to get points
        
        Returns:
            points (int): The amount of points the rank is worth
    """
    if len(r) == 1:
        rank = r[0]
    elif len(r) == 2:
        rank = r[0]
    else:
        rank = r
    if rank in ranks:
        return ranks[f'{rank}'][1]
    else:
        raise ValueError(f"invalid rank symbol: {rank}")


def rank_higher_than(r1: str, r2: str):
    """
    Checks if one rank is higher than another
    
        Parameters:
            r1 (str): The first rank which is compared
            r2 (str): The second rank which r1 is compared too
            
        Returns:
            answer (bool): Whether r1 is higher than r2
    """
    issue = None
    if len(r1) == 1:
        r1_rank = r1[0]
    elif len(r1) == 2:
        r1_rank = r1[0]
    else:
        r1_rank = r1
        
    if len(r2) == 1:
        r2_rank = r2[0]
    elif len(r2) == 2:
        r2_rank = r2[0]
    else:
        r2_rank = r2
    
    if r1_rank in ranks:
        r1_position = ranks[f'{r1_rank}'][2]
    else:
        issue = r1_rank
        raise ValueError(f"invalid rank symbol: {issue}")

    if r2_rank in ranks:
        r2_position = ranks[f'{r2_rank}'][2]
    else:
        issue = r2_rank
        raise ValueError(f"invalid rank symbol: {issue}")

    if r1_position < r2_position:
        return True
    else:
        return False
