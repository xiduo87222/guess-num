import random

r = random.randint(1, 100)
while True:
    guess = input('猜一個數字: ')
    guess = int(guess)
    if guess == r:
        print('猜對了!')
        break
    elif guess > r:
        print('比答案大')
    elif guess < r:
        print('比答案小')

