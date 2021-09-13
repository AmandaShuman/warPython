# This is the code to play the card game go Fish
import time
import random
from card_pkg.card_functions import full_deck, go_fish_ask, starting_hand, check_for_matches, values_only, who_wins, points_display, remove_paired_card
from card_pkg.game_rules import go_fish_rules


def check_game_end():
    if len(player_hand) == 0 or len(computer_hand) == 0:
        who_wins(player_score, computer_score, player_hand, computer_hand)

# go_fish_rules()


# setting up the game to begin play
player_hand, remaining_deck = starting_hand(full_deck(), 7)
computer_hand, remaining_deck = starting_hand(remaining_deck, 7)
player_hand.sort()
player_name = input("Enter your name: ")
computer_name = input(f"Thanks {player_name}! Now enter your challenger's name: ")
player_name = player_name.capitalize()
computer_name = computer_name.capitalize()
print(f"Here is {player_name}'s hand: {player_hand}\n")
time.sleep(2)
player_score = 0
computer_score = 0

# check for matches in hands of player and computer
print("""
Let's start by checking everyone's hands for matches...
""")
player_values = values_only(player_hand)
computer_values = values_only(computer_hand)

player_hand, player_score, player_values = check_for_matches(
    player_name, player_hand, player_score, player_values)

computer_hand, computer_score, computer_values = check_for_matches(
    computer_name, computer_hand, computer_score, computer_values)

points_display(player_score, computer_score, player_hand, computer_hand)

print("Now that the setup is done... it's time to play GO FISH!! \n")
time.sleep(1)

while True:
    # =======================================
    #            Player's turn
    # =======================================
    while True:
        print(f"Here is your hand:", player_hand)
        player_choice = go_fish_ask(player_values, player_name)

        # checking answer...
        if player_choice in computer_values:
            print(f"{computer_name} has a {player_choice}!")
            player_score += 2
            player_values.remove(player_choice)
            computer_values.remove(player_choice)
            player_hand = remove_paired_card(player_choice, player_hand)
            computer_hand = remove_paired_card(player_choice, computer_hand)
            points_display(player_score, computer_score,
                           player_hand, computer_hand)
            time.sleep(2)

            # end game if someone runs out of cards
            if len(player_hand) == 0 or len(computer_hand) == 0:
                check_game_end()
        else:
            print(f"{computer_name} doesn't have any {player_choice}s. Go Fish!")
            picked_up_card = remaining_deck[0][0]
            print("You picked up card:", remaining_deck[0])

            # if player picks up same card asked for and gets to go again
            if picked_up_card == player_choice:
                print(f"{player_name} picked up the card they asked for. Go again!")
                remaining_deck.pop(0)
                player_score += 2
                player_values.remove(player_choice)
                player_hand = remove_paired_card(player_choice, player_hand)
                if len(player_hand) == 0 or len(computer_hand) == 0:
                    check_game_end()
            else:
                player_hand.append(remaining_deck[0])
                player_values = values_only(player_hand)
                player_values.sort()
                remaining_deck.pop(0)
                player_hand, player_score, player_values = check_for_matches(
                    player_name, player_hand, player_score, player_values)
                points_display(player_score, computer_score,
                               player_hand, computer_hand)
                time.sleep(2)
                break

    # =======================================
    #            Computer's turn
    # =======================================
    if len(player_hand) == 0 or len(computer_hand) == 0:
        check_game_end()
    while True:
        computer_choice_index = random.randint(0, (len(computer_values)-1))
        computer_choice = computer_values[computer_choice_index]
        print(f"{computer_name} asks, do you have any {computer_choice}s?")
        if computer_choice in player_values:
            print(
                f"You have a {computer_choice} so you give it to {computer_name}. There's no cheating in this game!😁")
            computer_score += 2
            player_values.remove(computer_choice)
            computer_values.remove(computer_choice)
            player_hand = remove_paired_card(computer_choice, player_hand)
            computer_hand = remove_paired_card(computer_choice, computer_hand)
            points_display(player_score, computer_score,
                           player_hand, computer_hand)
            time.sleep(1)
            if len(player_hand) == 0 or len(computer_hand) == 0:
                check_game_end()
        else:
            print(f"{player_name} doesn't have any {computer_choice}s. Go Fish!!")
            picked_up_card_comp = remaining_deck[0][0]
            if picked_up_card == computer_choice:
                print(f"{computer_name} picked up the card they asked for. Go again!")
                remaining_deck.pop(0)
                computer_score += 2
                computer_values.remove(computer_choice)
                computer_hand = remove_paired_card(computer_choice, computer_hand)
                if len(player_hand) == 0 or len(computer_hand) == 0:
                    check_game_end()
            else:
                computer_hand.append(remaining_deck[0])
                computer_values = values_only(computer_hand)
                remaining_deck.pop(0)
                computer_hand, computer_score, computer_values = check_for_matches(
                    computer_name, computer_hand, computer_score, computer_values)
                points_display(player_score, computer_score,
                               player_hand, computer_hand)
                time.sleep(1)
                break

