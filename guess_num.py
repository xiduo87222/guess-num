import random

r = random.randint(1, 100)
count = 0 #計數
while True:
    count += 1 #count = count + 1 
    guess = input('猜一個數字: ')
    guess = int(guess)
    if guess == r:
        print('猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif guess > r:
        print('比答案大')
    elif guess < r:
        print('比答案小')
    print('這是你猜的第', count, '次') 