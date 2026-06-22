import random
def create_cards():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    random.shuffle(cards)
    return cards
def calculate_handScore(hand):
    score=sum(hand)
    
    while score>21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score=sum(hand)

    return score

def draw_card(deck):
    return deck.pop()

def blackJack():
    chips=100
    print("\n Your chips: ",chips)
    while chips >0 :
        
        bet= int(input( "Enter your bet: "))
        while bet>chips or bet <=0:
            print("\n Invalide bets ! ")
            bet = input(print("Enter your bet: "))
            
        deck=create_cards()
        player=[draw_card(deck),draw_card(deck)]
        dealer=[draw_card(deck),draw_card(deck)]
        game_over= False
        
        while not game_over:
            player_score=calculate_handScore(player)
            dealer_score=calculate_handScore(dealer)
            
            print("\nYour cards:",player,"Score:",player_score)
            print ("Dealer cards:",dealer,"Score:",dealer[0])
            
            if player_score >21:
                print("BUSTED")
                return
            
            choice = input("Hit card (Y) or stay(N) ? : ")
            if choice.lower()=="y":
                player.append(draw_card(deck))
            else:
                game_over=True
        
        while calculate_handScore(dealer) < 17:
            dealer.append(draw_card(deck))
            
        player_score=calculate_handScore(player)
        dealer_score=calculate_handScore(dealer)
            
        print("\nPlayer:",player,"Score:",player_score)
        print("Dealer:",dealer,"Score:",dealer_score)
        
        if dealer_score > 21:
            print("Dealer busted , YOU WIN !")
            chips+=bet
            
        elif player_score>21:
            print("BSUTED , Dealer Win !")
            chips-=bet
            
        elif player_score > dealer_score:
            print("YOU WIN !")
            chips+=bet
            
        elif dealer_score > player_score:
            print("DEALER Win !")
            chips-=bet
            
        elif player_score == 21:
            print("BLACK JACK,YOU WIN")
            chips+=bet*1.5
            break
            
        else:
            print("DRAW")
        
        print(f"Raimaining chips: {chips}")
        if chips == 0 :
            print("Game Over!, you ran out of chips.")
        
        
        
while True:                                               
    blackJack()
    again = input("\nPlay again? (Y/N): ")
    if again.lower() != "y":
        print("Thanks for playing. Goodbye!")
        break
    
    