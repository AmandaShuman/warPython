# This is the code to play the card game go Fish
import time
import random
from card_pkg.card_functions import full_deck, go_fish_ask, starting_hand, check_for_matches, values_only, go_fish_check, keep_playing
from card_pkg.game_rules import go_fish_rules


def points_display(player_score, computer_score, player_hand, computer_hand):
    print(f"""---------------------------------------------
Scores:         You: {player_score}      || Computer: {computer_score}
---------------------------------------------
Card Count:     You: {len(player_hand)}      || Computer: {len(computer_hand)}
---------------------------------------------
    """)

# go_fish_rules()


# setting up the game to begin play
player_hand, remaining_deck = starting_hand(full_deck(), 7)
computer_hand, remaining_deck = starting_hand(remaining_deck, 7)
player_hand.sort()
player_name = input("Enter your name: ")
player_name = player_name.capitalize()
print(f"Here is {player_name}'s hand: {player_hand}\n")
time.sleep(2)
player_score = 0
computer_score = 0

# check for matches in hands of player and computer
print("Checking for matches now...")
player_hand, player_score = check_for_matches(player_name, player_hand, player_score)
computer_hand, computer_score = check_for_matches("The computer", computer_hand, computer_score)
points_display(player_score, computer_score, player_hand, computer_hand)

print("Now that the setup is done... it's time to play GO FISH!! \n")
time.sleep(2)
""" TO DO
Check computer values to see if match
    if no match - give free turn if card picked up is the same one as was asked for
"""

while True:
    # condition for end of game
    if len(player_hand) == 0 or len(computer_hand) == 0:
        print("The game is over!")
        if player_score > computer_score:
            print("You've won! Congrats!!")
        elif computer_score > player_score:
            print("The computer has won this round. Try again.")
        else:
            print("It's a tie!")
        break
    # condition to play
    else:
        # =======================================
        #            Player's turn
        # =======================================
        while True:
            player_values = values_only(player_hand)
            computer_values = values_only(computer_hand)
            player_choice = go_fish_ask(player_values, player_name)
            #  card_pick = random.randint(0, (len(remaining_deck)-1))
            if player_choice in computer_values:
                print(f"The computer has a {player_choice}!")
                player_score += 2
                player_values.remove(player_choice)
                computer_values.remove(player_choice)
                player_hand = [card for card in player_hand if card[0] in player_values]
                computer_hand = [card for card in computer_hand if card[0] in computer_values]
                points_display(player_score, computer_score, player_hand, computer_hand)
                time.sleep(2)
                if len(player_hand) == 0 or len(computer_hand) == 0:
                    break
            else:
                print(f"The computer doesn't have any {player_choice}s. Go Fish!")
                picked_up_card = remaining_deck[0][0]
                print("You picked up card:", remaining_deck[0])

                # if player picks up same card asked for and gets to go again
                if picked_up_card == player_choice:
                    print(f"{player_name} picked up the card they asked for. Go again!")
                    remaining_deck.pop(0)
                    player_score += 2
                    player_values.remove(player_choice)
                    if len(player_hand) == 0 or len(computer_hand) == 0:
                        break
                else:
                    player_hand.append(remaining_deck[0])
                    remaining_deck.pop(0)
                    player_hand, player_score = check_for_matches(player_name, player_hand, player_score)
                    points_display(player_score, computer_score, player_hand, computer_hand)
                    time.sleep(2)
                    break

        # =======================================
        #            Computer's turn
        # =======================================
        if len(player_hand) == 0 or len(computer_hand) == 0:
            break
        while True:
            player_values = values_only(player_hand)
            computer_values = values_only(computer_hand)
            computer_choice_index = random.randint(0, (len(computer_values)-1))
            computer_choice = computer_values[computer_choice_index]
            #  card_pick = random.randint(0, (len(remaining_deck)-1))
            print(f"The computer asks, do you have any {computer_choice}s?")
            if computer_choice in player_values:
                print(f"You have a {computer_choice} so you give it to the computer. There's no cheating in this game!😁")
                computer_score += 2
                player_values.remove(computer_choice)
                computer_values.remove(computer_choice)
                player_hand = [
                    card for card in player_hand if card[0] in player_values]
                computer_hand = [
                    card for card in computer_hand if card[0] in computer_values]
                points_display(player_score, computer_score, player_hand, computer_hand)
                time.sleep(1)
                if len(player_hand) == 0 or len(computer_hand) == 0:
                    break
            else:
                print(f"{player_name} doesn't have any {computer_choice}s. Go Fish!!")
                computer_hand.append(remaining_deck[0])
                remaining_deck.pop(0)
                computer_hand, computer_score = check_for_matches("The computer", computer_hand, computer_score)
                points_display(player_score, computer_score, player_hand, computer_hand)
                time.sleep(1)
                break


                
        # player_hand, computer_hand, remaining_deck, player_score = go_fish_check(player_choice, player_score, player_hand, "The computer", computer_hand, remaining_deck)
