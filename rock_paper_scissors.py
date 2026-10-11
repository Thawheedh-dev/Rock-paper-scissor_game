import random
game=['rock', 'paper', 'scissors']

while True:
    random_choice = random.choice(game)
    choose=input("Enter rock, scissors ,paper:")
    if choose==random_choice:
        print("Draw")
        print(random_choice)
    elif choose=="rock" and random_choice=="paper" :
        print("you lose")
        print(random_choice)
    elif  choose=='paper' and random_choice=='scissors':
        print("you lose")
        print(random_choice)
    elif choose=='scissor' and random_choice=='rock':
        print("you lose")
        print(random_choice)

    elif choose=='scissors' and random_choice=='paper' :
        print("You win")
        print(random_choice)
    elif choose=='paper' and random_choice=='scissors':
        print("You win")
        print(random_choice)
    elif choose=='rock' and random_choice=='scissors':
        print("You win")
        print(random_choice)