import sueca_suits_ranks as sr
import sueca_cards as sc
import sueca_tricks as st
import sueca_games as sg

class SuecaGameIncomplete(Exception):
    pass
class GameFileCouldNotBeFound(Exception):
    pass

def runGame(fname, showCards = False, showGame = False):
    
    try:
        tc, ts = st.parseGameFile(fname)
        g = sg.Game(tc)
    except FileNotFoundError:
        raise GameFileCouldNotBeFound(f"Could not find the game file '{fname}'")
    
    if len(ts) < 10:
        raise SuecaGameIncomplete(f"Game file '{fname}' is incomplete. A complete game takes 10 rounds; the given game includes {len(ts)} rounds only.")
        
    
    for t in ts:
        g.playTrick(t)
    
    score = list(g.score())
    
    all_cards = [] 
    for i in range(4):
        for card in g.cardsOf(i+1):
            all_cards.append(card.show())
    
    player1 = all_cards[:10]
    player2 = all_cards[10:20]
    player3 = all_cards[20:30]
    player4 = all_cards[30:40]
    
    final_cards = []
    final_cards.append(player1)
    final_cards.append(player2)
    final_cards.append(player3)
    final_cards.append(player4)
    
    final_cards_str = []
    
    for i in range(len(final_cards)):
        final_cards_str.append(f"Player {i+1}: {', '.join(final_cards[i])}")
            
    a = []
    for i in range(10):
        a.append(g.gameTricks()[i].show())
    
        
    
    if score[0] > score[1]:
        winner = f"Pair A won the given sueca game\nScore: {score[0]} - {score[1]}"
    elif score[0] == score[1]:
        winner = f"The game resulted in a draw\nScore: {score[0]} - {score[1]}"
    else:
        winner = f"Pair B won the given sueca game\nScore: {score[0]} - {score[1]}"
    
    if showCards == False and showGame == False:
        print(winner)
        
    elif showCards == True and showGame == False:
        print(winner)
        print("Player's cards in the sueca game")
        for i in final_cards_str:
            print(i)
                
    elif showCards == False and showGame == True:
        output = []
        output.append(winner)
        trump = g.gameTrump().show()
        trump_name = sr.suit_full_name(trump)
        output.append(f"Trump: {trump} - {trump_name}")
        for i in range(len(a)):
            output.append(f"{i+1}: {a[i]}")
        
        for o in output:
            print(o)
    else:
        print(winner)
        output = []
        trump = g.gameTrump().show()
        trump_name = sr.suit_full_name(trump)
        print(f"Trump: {trump} - {trump_name}")
        print("Player's cards in the sueca game")
        for i in final_cards_str:
            print(i)
        output = []
        for i in range(len(a)):
            output.append(f"{i+1}: {a[i]}")
        
        for o in output:
            print(o)
    

