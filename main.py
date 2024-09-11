import random
print("Assalamualikum,Welcome to the guessing game::")
print("I am going to think of a number between 1 and 100 and you have to guess it")
toprange=input("Type a Number upto which range: ")

if toprange.isdigit():
    toprange=int(toprange)
    if toprange<=0:
        print("Type a Number larger than 0 nect time:")
else:
    print("Please type a number next time")
    quit()



randomnumber = random.randint(0,toprange)

guess=0
while True:
    guess+=1
    toprange
    user_guess=input("Enter the Digit to guess the number below what you chose range::")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if randomnumber==user_guess:
            print("YOu Got it")
            break
        elif user_guess>randomnumber:
            print("Try again")
            print("The guess number is above")
        else:
            print("The guess number is below")
print("Your guess is right  guess",guess)