# Armaan Singh Brar
# Final Project
# Black Jack

import random
money = 0

card_dict = {'2 of Diamond':2,
            '2 of Spades':2,
            '2 of Clubs':2,
            '2 of Hearts':2,
            '3 of Diamond':3,
            '3 of Spades':3,
            '3 of Clubs':3,
            '3 of Hearts':3,
            '4 of Diamond':4,
            '4 of Spades':4,
            '4 of Clubs':4,
            '4 of Hearts':4,
            '5 of Diamond':5,
            '5 of Spades':5,
            '5 of Clubs':5,
            '5 of Hearts':5,
            '6 of Diamond':6,
            '6 of Spades':6,
            '6 of Clubs':6,
            '6 of Hearts':6,
            '7 of Diamond':7,
            '7 of Spades':7,
            '7 of Clubs':7,
            '7 of Hearts':7,
            '8 of Diamond':8,
            '8 of Spades':8,
            '8 of Clubs':8,
            '8 of Hearts':8,
            '9 of Diamond':9,
            '9 of Spades':9,
            '9 of Clubs':9,
            '9 of Hearts':9,
            '10 of Diamond':10,
            '10 of Spades':10,
            '10 of Clubs':10,
            '10 of Hearts':10,
            'J of Diamond':10,
            'J of Spades':10,
            'J of Clubs':10,
            'J of Hearts':10,
            'Q of Diamond':10,
            'Q of Spades':10,
            'Q of Clubs':10,
            'Q of Hearts':10,
            'K of Diamond':10,
            'K of Spades':10,
            'K of Clubs':10,
            'K of Hearts':10,
            'A of Diamond':11,
            'A of Spades':11,
            'A of Clubs':11,
            'A of Hearts':11}

def main():
    while True:
        try:
            add = int(input("How money would you like to deposit : "))
            break
        except ValueError:
            print("Please Enter a Valid Number!")

    money = get_money(add)
    cards = generate_cards()

    table = input("Choose a table: \n1. Starter table : 5$ \n2. Middle End Table : 100$ \n3. High Rollers Table : 500$\n=")
    base_wager = get_limits(table)
    sums = BlackJackStart(cards, base_wager, money)
    outcome = Outcome(sums)
    outcome = Result(outcome,sums)
    BlackJackContinue(outcome, sums[2], sums)



def generate_cards():
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['Diamond','Spades','Clubs','Hearts']
    cards = []
    for i in ranks:
        for j in suits:
            cards.append(f"{i} of {j}")
    return cards


def get_limits(table):
    if table == "1":
        return 5
    elif table == "2":
        return 100
    elif table == "3":
        return 500
    else:
        print("Enter a Valid Table Number")
        get_limits()


def BlackJackStart(cards, base_wager, money):
    if money < base_wager:
         money = get_money()
    while True:
        try:
            wager = int(input("Place your Wager : "))
            break
        except ValueError:
            print("Enter a Proper Wager!")
    player_sum = 0
    dealer_sum = 0
    player_cards = []
    dealer_cards = []
    for _ in range(2):
        player_card = random.choice(cards)
        cards.remove(player_card)
        dealer_card = random.choice(cards)
        cards.remove(dealer_card)
        player_cards.append(player_card)
        dealer_cards.append(dealer_card)
        player_sum += card_dict[player_card]
        dealer_sum += card_dict[dealer_card]

    print("\n\nYour Cards are : ")
    for i in player_cards:
        print(i)

    return [player_sum,dealer_sum,cards,wager,money,player_cards,dealer_cards]



def Outcome(sums):
    player_sum = sums[0]
    dealer_sum = sums[1]
    if player_sum == 21:
        if dealer_sum == 21:
            return "Draw"
        else:
            return "Win"
    elif dealer_sum == 21:
        return "Loss"
    elif dealer_sum > 21:
        return "Win"
    elif player_sum >21:
        return "Loss"
    else:
        return "Continue"


def Result(outcome,sums):
    if outcome == "Win":
        print(f"\nDealers cards: ")
        for i in sums[6]:
            print(i)
        print(f"\nYour total : {sums[0]}")
        print(f"Dealers total {sums[1]}")
        print("\n\nYou won the match!")
        sums[4] += sums[3]
        money = sums[4]
        print(f"Total money = {sums[4]}")
        return [money,0]
    elif outcome == "Loss":
        print(f"\nDealers cards: ")
        for i in sums[6]:
            print(i)
        print(f"\nYour total : {sums[0]}")
        print(f"Dealers total : {sums[1]}")
        print("\n\nYou lost the match")
        sums[4] -= sums[3]
        money = sums[4]
        print(f"Total money = {sums[4]}")
        return [money,0]
    elif outcome == "Surrender":
        sums[4] -= (sums[3])/2
        money = sums[4]
        print(f"Total money = {sums[4]}")
        return [money,0]
    elif outcome == "Continue":
        return [1,1]


def BlackJackContinue(outcome, cards, sums):
    if outcome[1] == 0:
        play_more()
    elif outcome[1] == 1:
        play = input("\n\nHow would you like to proceed? \n1. Hit \n2. Stand \n3.Surrender \n=")
        if play == "3":
            Result("Surrender",sums)
            play_more()
        elif play == "2":
            final_result = final_outcome(sums)
            Result(final_result, sums)
            play_more()
        elif play == "1":
            player_sum = sums[0]
            dealer_sum = sums[1]
            player_cards = sums[5]
            dealer_cards = sums[6]
            player_card = random.choice(cards)
            cards.remove(player_card)
            dealer_card = random.choice(cards)
            cards.remove(dealer_card)
            player_cards.append(player_card)
            dealer_cards.append(dealer_card)
            player_sum += card_dict[player_card]
            dealer_sum += card_dict[dealer_card]

            sums[0] = player_sum
            sums[1] = dealer_sum
            sums[5] = player_cards
            sums[6] = dealer_cards

            print("\n\nYour Cards are : ")
            for i in player_cards:
                print(i)

            outcome = Outcome(sums)
            if outcome == "Draw":
                outcome = final_outcome(sums)
                outcome_1 = Result(outcome, sums)
                BlackJackContinue(outcome_1, cards, sums)
            else:
                outcome_1 = Result(outcome, sums)
                BlackJackContinue(outcome_1, cards, sums)





def final_outcome(sums):
    if sums[0] > sums[1]:
        return "Win"
    elif sums[1] >= sums[0]:
        return "Loss"


def play_more():
    response = input("\n\nWould you like to play further (yes/no)? ")
    if response == "yes":
        main()
    elif response == "no":
        pass
    else:
        print("Enter only of the given option!")
        play_more()


def get_money(add):
    return money+add



if __name__ == "__main__":
    main()
