import time
import random

rand = random.randint(1, 4)
time.sleep(10)

if rand == 1:
        animatronic = True
else:
        animatronic = False

if animatronic == True:
        print ("ohmy god theyre gonna get me")
elif animatronic == False:
        print("nothing happened")
print("There are intruders and now they're inside your house. Stay alive in your bedroom until sunrise to survive. they will activitly search for blUd. movement will increase his awareness ")
print("everytime you open the flashlight their awarness will increase. if you keep hiding in your closet, it has a higher chance the pone ring which increase the chance of them comin")
print("Frequently check each camera to spot them")
choice = int(input("Where would you like to check? :Doorway(1): :Closet(2): :Under your bed(3):"))
while animatronic == False:
    start = time.time()
    while True:
        elapsed = time.time() 
        
        if elapsed >= 30:
            break


        time.sleep(0.1)

    print("\nStopped after 10 seconds.")

if choice == "1":
    if animatronic == True:
        input("aaahhh quick use flashlight ")
    else:
        input("nothing here. go back? (Y/N)")