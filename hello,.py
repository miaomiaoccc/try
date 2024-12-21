import random
print("Hello, GPT!")
name = input("What's your name? ")
print(f"Hello, {name}!")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The sum is: {num1 + num2}")
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult!")
else:
    print("You are still a minor!")

number = random.randint(1, 100)
max_attempts = 5  # 最大猜测次数
attempts = 0  # 当前已经猜了几次

print("Guess a number between 1 and 100! You have 5 attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1  # 每猜一次，增加一次计数

    if guess == number:
        print("You guessed it!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    # 如果达到最大次数
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts! The number was {number}.")



