#Julissa Franco
#02.28.2019
#Beginning Chapter 1
#Zombie Escape
import random


print ("Welcome!")

print ("Choose your players and type the name for your players")

print("Gender of players? ")
d1a = input("Choose: A) Male and Male B) Female and Male C)Female and Female [A/B/C]? : ")
##if d1a == "A":
##            print ("Choose:")
##elif d1a == "B":
##            print ("Choose:")
##elif d1a == "C":
##            print ("Choose:")
##    else
name1 = input("Name of player one ")
name2 = input("Name of player two ")
       
print("A city has been infected with a virus that is turning the population into zombies. Two individuals will do what it takes to escape the city with your help.Are you ready to play", name1, " and ", name2)

print("Chapter 1:", name1, " and ", name2, "Your mission is to decide which location you will travel to make your way out of the city. You must choose wisely.") 


print("Choose your escape ")
street = input("Choose: A) Elm Street  B) Main Street C) Doom Street [A/B/C]? : ")

#Player will choose weapons

print("Great! Now you will choose the weapons you will use to defend your player from the zombies")

def weapon():
    print("Player 1, choose your weapons")

    global weapon1 # needs to be global to reference outside of the function
    weapon1 = input("Choose: A) Gun B) Knife C)Chainsaw [A/B/C]? : ")

    print("Player 2, choose your weapons")

    global weapon2 # needs to be global to reference outside of the function
    weapon2 = input("Choose: A) Gun B) Knife C)Chainsaw [A/B/C]? : ")

    print("Now that you have chose your weapons, it is time for your escape" , name1, "and", name2, "Are you ready to leave the house?")

    # Made change here - Fixed NameError: name 'leave' is not defined
    # (this was due to referencing leave below in the if statement
    # it was previously only defined for use within the function
    global leave
    leave = input("Choose: A) Yes  B) No [A/B]? : ")

weapon()
if leave == "A":
    print("It seems that you are ready for your escape.")


#Chapter 2 Starts Here

print("Chapter 2:", name1, " and ", name2, " are hiding behind a bush and encounter their first zombie. Their mission is to kill the zombie to move on to chapter 3.")

print("the zombie stands behind both player.", name1, "It is your time to try to kill the zombie")

zombieStatus = "alive" # Added for a check for moving to chapter 3
# Adding in while loop will allow the following to occur till the zombie dies
while zombieStatus == "alive":
    if weapon1 == "A": # Dedented this line
        x = random.randrange(1, 10) # Dedented this line
        if x < 6:
            print("zombie is hurt but still alive")

    elif weapon1 == "B":
    
        x = random.randrange(1, 10)
        if x < 2:
            print("zombie is still alive")

    else: # Never have anything else in the else statement
        x = random.randrange(1, 10)
        if x < 8:
            zombieStatus = "dead"
            print("zombie dies")
#If player 1 kills zombie, chapter 3 begins
    if zombieStatus == "alive":
        print("You partner needs your help", name2, "finish the zombie")
        if weapon2 == "A":
            x = random.randrange(1, 10)
            if x < 6:
                print("zombie is hurt but still alive")

        elif weapon2 == "B":
            x = random.randrange(1, 10)
            if x < 2:
                print("zombie is still alive")

        else:
            x = random.randrange(1, 10)
            if x < 8:
                zombieStatus = "dead"
                print("zombie dies")

print("You have defeated your first zombie you are now ready to move on to chapter 3")

#Chapter 3 starts here

print("You will now face one of the challenging chapters. Will both players survive? Will one player survive and escape?")

 #Players are surrounded by 3 zombies
zombiecount = 3

while zombiecount!= 0 :
    zombieStatus = "alive" 

    while zombieStatus == "alive":
        if weapon1 == "A": 
            x = random.randrange(1, 10) 
            if x < 4:
                print("zombie is hurt but still alive")

        elif weapon1 == "B":
            x = random.randrange(1, 10)
            if x < 9:
                print("zombie is still alive")

        else: 
            x = random.randrange(1, 10)
            if x < 6:
                zombieStatus = "dead"
                print("zombie dies")

        if zombieStatus == "alive":
            print("You partner needs your help", name2, "finish the zombie")
            if weapon2 == "A":
                x = random.randrange(1, 10)
                if x < 3:
                    print("zombie is hurt but still alive")

            elif weapon2 == "B":
                x = random.randrange(1, 10)
                if x < 7:
                    print("zombie is still alive")

            else:
                x = random.randrange(1, 10)
                if x < 4:
                    zombieStatus = "dead"
                    print("zombie dies")

                    zombiecount-=1
print("Awsome! Great teamwork! You will now move on to chapter 4")

#Chapter 4 Starts here

print("Chapter4:", name1, " and ", name2, " You are a chapter closer into escaping the city. You must run and kill when coming in contacting a zombie. Don't let the zombie catch you")

zombieStatus = "alive" 
while zombieStatus == "alive":

    if weapon1 == "A":
        x = random.randrange(1, 10)
        if x < 9:
            print("zombie is hurt but still alive")

    elif weapon1 == "B":
        x = random.randrange(1, 10)
        if x < 3:
            print("zombie is still alive")

    else: 
        x = random.randrange(1, 10)
        if x < 4:
            zombieStatus = "dead"
            print("zombie dies")
  
    if zombieStatus == "alive":
        print("Help your partner", name2, "finish the zombie")
        if weapon2 == "A":
            x = random.randrange(1, 10)
            if x < 6:
                print("zombie is hurt but still alive")

        elif weapon2 == "B":
            x = random.randrange(1, 10)
            if x < 7:
                print("zombie is still alive")

        else:
            x = random.randrange(1, 10)
            if x < 8:
                zombieStatus = "dead"
                print("zombie dies")


#Chapter 5 Starts here

print("Chapter5:", name1, " and ", name2, " This your chance to finally make your escape! Don't let anything stop you!")
print("It seems that the coast is clear! Make your run now")
print("Oh no! There's a zombie behind. Kill it!")

zombieStatus = "alive"
      
while zombieStatus == "alive":
    if weapon1 == "A": 
        x = random.randrange(1, 10)
        if x < 8:
            print("zombie is hurt but still alive")

    elif weapon1 == "B":
        x = random.randrange(1, 10)
        if x < 1:
            print("zombie is still alive")

    else: 
        x = random.randrange(1, 10)
        if x < 4:
            zombieStatus = "dead"
            print("zombie dies")

    if zombieStatus == "alive":
        print("You partner needs your help", name2, "finish the zombie")
        if weapon2 == "A":
            x = random.randrange(1, 10)
            if x < 9:
                print("zombie is hurt but still alive")

        elif weapon2 == "B":
            x = random.randrange(1, 10)
            if x < 6:
                print("zombie is still alive")

        else:
            x = random.randrange(1, 10)
            if x < 2:
                zombieStatus = "dead"
                print("zombie dies")

print("You killed the zombie! Now is your time to run through the forest! Once you have reached the forest, you have finally escape the city!")

print("Congratulations! You saved yourselves!")




                    
