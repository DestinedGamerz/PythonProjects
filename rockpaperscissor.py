import random

game_choices = ['Rock', 'Paper', 'Scissors']

pick = random.choice(game_choices)

choose = input("Please enter a value: ")

if pick == 'Rock' and choose == 'Rock':
    print("It's a tie")

if pick == 'Rock' and choose == 'Paper':
    print("Player wins")

if pick == 'Rock' and choose == 'Scissors':
    print("Computer Wins")

if pick == 'Paper' and choose == 'Paper':
    print("It's a tie")

if pick == 'Paper' and choose == 'Scissors':
    print("Player wins")

if pick == 'Paper' and choose == 'Rock':
    print("Computer Wins")

if pick == 'Scissors' and choose == 'Scissors':
    print("It's a tie")

if pick == 'Scissors' and choose == 'Rock':
    print("Player wins")

if pick == 'Scissors' and choose == 'Paper':
    print("Computer Wins")

print("The computer picked", pick)