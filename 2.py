import random

print("------Game start------ ")
value=random.randint(1, 101)
for i in range(1,11):
    print(f"You have {11-i} Chance to guess the number ")
    user=int(input("Enter number: "))
    if value==user:
        break
    elif user<value:
        print("Your guess is wrong,Try Higher number!")
    elif user>value:
        print("Your guess is wrong,Try Lower number!")
    
if value==user:
    print("CONGRATULATION YOU WON")
else:
    print("YOU LOSS")
    #HIIIIIIIIIIIIIII