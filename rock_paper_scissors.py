import random

print("WELCOME TO ROCK PAPER SCISSORS!")

player_score = 0
computer_score = 0
game_on = True

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

while game_on:
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
        if choice < 0 or choice > 2:
            print("Invalid choice. Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    user_choice = choice
    computer_choice = random.randint(0, 2)

    print(f"\nYou chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It is a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

    if player_score == 10:
        print("🎉 You won the game! 🎉")
        game_on = False
    elif computer_score == 10:
        print("💻 Computer won the game. Better luck next time!")
        game_on = False
