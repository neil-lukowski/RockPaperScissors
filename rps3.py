p1_wins = 0
p2_wins = 0
ties = 0

def victor(winner):
    output = ("\nPlayer "+ str(winner)+ " wins: ")
    return output


def one_game(p1, p2):
    global p1_wins
    global p2_wins
    global ties
    
    rvs = 'Rock crushes Scissors'
    rvp = 'Paper covers Rock'
    svp = 'Scissors cuts Paper'
    tis = 'Tie: Scissors ties Scissors'
    tir = 'Tie: Rock ties Rock'
    tip = 'Tie: Paper ties Paper'
    
    if p1 == p2:
        ties +=1
        if p1 == 1:
            print(tip)
        elif p1 == 2:
            print(tis)
        else:
            print(tir)
    
    if p1 == 0 and p2 == 2:
        p1_wins += 1
        print(victor(1) + rvs)
    elif p1 == 2 and p2 == 0:
        p2_wins +=1
        print(victor(2) + rvs)

    if p1 == 2 and p2 == 1:
        p1_wins += 1
        print(victor(1) + svp)
    elif p1 == 1 and p2 == 2:
        p2_wins +=1
        print(victor(2) + svp)

    if p1 == 1 and p2 == 0:
        p1_wins += 1
        print(victor(1) + rvp)
    elif p1 == 0 and p2 == 1:
        p2_wins +=1
        print(victor(2) + rvp)

def main():
    
    game = int(input("Do you want to play the game (0 for yes; 1 for no)?"))
    
    while game == 0:
        p1_choice = int(input("\nPlayer 1: Enter Rock (0), Paper(1), Scissors (2): "))
        p2_choice = int(input("\nPlayer 2: Enter Rock (0), Paper(1), Scissors (2): "))
        one_game(p1_choice, p2_choice)
        game = int(input("\nDo you want to play the game (0 for yes; 1 for no)?"))

    print('\nThanks for playing. Player 1 won', str(p1_wins), "games Player 2 won", str(p2_wins), "games.", str(ties), 'tie.')

main()