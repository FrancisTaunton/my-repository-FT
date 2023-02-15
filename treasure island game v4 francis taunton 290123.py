print("Treasure Island the Game.")
print("To win the game choose correctly.")
#why can't i get these loops to work?!!? Bring back BASIC. I could just type goto line xyz! annoying.
#Fergus I got most frustrated with this. Why can an If/else routine only print something? why can't i get it to Go/do somewhere else? 
#all these loops seem messy to me.
#i'm wasting my life on this. ending now. basically works.
while True:
    direction = input("You're are on treasure island. First you have to pick a route. \n Type 'left' or 'right' to pick.\n").lower()
    if direction == "left":
        while True:
#continues the game next choice
            action = input("Good choice. Your next decision is to swim to the next task or wait. \n Type 'swim' or 'wait' ?\n").lower()
            if action == "wait":
#continues the game. sets up a while loop
                while True:
                    colour = input("After waiting a while you walk on. \n Suddenly three doors appear. They are Red, Yellow and Blue. Pick one. \n Type 'red' or 'yellow' or 'blue' \n").lower()
                    if colour == "yellow":
#positive ending
                        print("^^^ Incredible! You have won ! ^^^")
                        print("^^^ Thank you for Playing this exciting game^^^")
                        exit()
#negative ending three ways or error return to start.
                    elif colour == "blue":
                        print("A terrible shame. You were eaten by a Giant Python.")
                        print("Unlucky, try again")
                        break
                        #i want to go back to the start here
                        quit()
                                                                        
                    elif colour == "red":
                        print("Ouch! It was a little toasty behind the red door. You roasted.")
                        print("Unlucky, try again")
                        break
                        quit()
    
                        
                    elif colour == False:
                        print("error, try again")
                        break
                
#negative ending 2nd choice action
            if action == "swim":
                print("***Game over!!! You were attcked by a giant trout. Sad times.***\n")
                print("Unlucky, try again")
                break
                quit()
            elif action == False:
                print("error, try again")
                break
#negative ending 1st choice direction
    if direction == "right":
        print("*****Game over!!!! You have fallen into a hole!!!*****\n ")
        print("Unlucky, try again")
        quit()
        break
    elif direction == False:
        print("error, try again")
        break
