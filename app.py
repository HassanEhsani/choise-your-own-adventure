name = input("Type your name: ")
print("welcome",name,"to this adventure! ")

answer = input("you are on a dirt road, it has come to an end and  you can go left or right, which way you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross:")
    
    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif answer == "walk": 
        print("You walked for many miles, ran out of water and you lost the game.")   
elif answer == "right":
    
else:
    print("Not a valid option. you lose.")



