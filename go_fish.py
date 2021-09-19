# This is the code to play the card game go Fish
import time
import random
from card_pkg.card_functions import full_deck, go_fish_ask, starting_hand, check_for_matches, values_only, who_wins, points_display, remove_paired_card, keep_playing
from card_pkg.game_rules import go_fish_rules


def check_game_end():
    if len(player_hand) == 0 or len(computer_hand) == 0:
        who_wins(player_score, computer_score, player_hand, computer_hand, rounds_played)

go_fish_rules()


# setting up the game to begin play
player_hand, remaining_deck = starting_hand(full_deck(), 7)
computer_hand, remaining_deck = starting_hand(remaining_deck, 7)
player_hand.sort()
player_name = input("Enter your name: ")
player_name = player_name.capitalize()
computer_name = input(
    f"Thanks {player_name}! Now enter your challenger's name: ")
computer_name = computer_name.capitalize()

while True:
    difficulty_setting = input(
        f"What difficulty mode would you like? 'Easy' or 'Hard': ")
    difficulty_setting = difficulty_setting.capitalize()
    if difficulty_setting == "Easy" or difficulty_setting == "Hard":
        print(
            f"You have chosen to play the {difficulty_setting} setting. Good luck!")
        break
    else:
        print("You may only enter Easy or Hard. Try again.")

print(f"Here is {player_name}'s hand: {player_hand}\n")
time.sleep(2)
player_score = 0
computer_score = 0
rounds_played = 0

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

points_display(player_score, computer_score, player_hand, computer_hand, rounds_played)

print("Now that the setup is done... it's time to play GO FISH!! \n")
time.sleep(1)

while True:
    # =======================================
    #            Player's turn
    # =======================================
    while True:
        print(f"Here is your hand:", player_hand)
        player_choice = go_fish_ask(player_values, player_name)
        computer_check = []
        computer_check.append(player_choice)  # for hard level
        rounds_played += 1

        # checking answer...
        if player_choice in computer_values:
            print(f"{computer_name} has a {player_choice}!")
            computer_check.remove(player_choice)
            player_score += 2
            player_values.remove(player_choice)
            computer_values.remove(player_choice)
            player_hand = remove_paired_card(player_choice, player_hand)
            computer_hand = remove_paired_card(player_choice, computer_hand)
            points_display(player_score, computer_score,
                           player_hand, computer_hand, rounds_played)
            time.sleep(2)

            # end game if someone runs out of cards
            if len(player_hand) == 0 or len(computer_hand) == 0:
                check_game_end()
        else:
            print(f"{computer_name} doesn't have any {player_choice}s. Go Fish!")
            picked_up_card = remaining_deck[0][0]
            print("You fished card:", remaining_deck[0])

            # if player picks up same card asked for and gets to go again
            if picked_up_card == player_choice[0]:
                print(f"{player_name} picked up the card they asked for. Go again!")
                computer_check.remove(player_choice)
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
                               player_hand, computer_hand, rounds_played)
                time.sleep(2)
                break

    # =======================================
    #            Computer's turn
    # =======================================
    if len(player_hand) == 0 or len(computer_hand) == 0:
        check_game_end()
    while True:
        # Easy or Hard - computer chooses different things
        if difficulty_setting == "Easy":
            computer_choice_index = random.randint(0, (len(computer_values)-1))
            computer_choice = computer_values[computer_choice_index]
        # TO DO
        else:
            # remove doubles from list of values player has asked for
            computer_check.sort()
            for card in computer_check:
                if computer_check.count(card) > 1:
                    computer_check.remove(card)

            overlap_check = computer_check + computer_values
            overlap_check.sort()
            overlap_list = []
            for value in overlap_check:
                if overlap_check.count(value) > 1:
                    overlap_list.append(value)
                    overlap_check.remove(value)
                    overlap_check.remove(value)
            if overlap_list == []:
                computer_choice_index = random.randint(
                    0, (len(computer_values)-1))
                computer_choice = computer_values[computer_choice_index]
            else:
                computer_choice_index = random.randint(
                    0, (len(overlap_list)-1))
                computer_choice = overlap_list[computer_choice_index]
                computer_check.remove(computer_choice)

        rounds_played += 1
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
                           player_hand, computer_hand, rounds_played)
            time.sleep(1)
            if len(player_hand) == 0 or len(computer_hand) == 0:
                check_game_end()
        else:
            print(f"{player_name} doesn't have any {computer_choice}s. Go Fish!!")
            picked_up_card_comp = remaining_deck[0][0]
            if picked_up_card_comp == computer_choice[0]:
                print(
                    f"{computer_name} picked up the card they asked for. Go again!")
                remaining_deck.pop(0)
                computer_score += 2
                computer_values.remove(computer_choice)
                computer_hand = remove_paired_card(
                    computer_choice, computer_hand)
                if len(player_hand) == 0 or len(computer_hand) == 0:
                    check_game_end()
            else:
                computer_hand.append(remaining_deck[0])
                computer_values = values_only(computer_hand)
                remaining_deck.pop(0)
                computer_hand, computer_score, computer_values = check_for_matches(
                    computer_name, computer_hand, computer_score, computer_values)
                points_display(player_score, computer_score,
                               player_hand, computer_hand, rounds_played)
                time.sleep(1)
                break

    keep_playing()
