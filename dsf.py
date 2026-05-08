import time
animatronic = False
print("There are inturders and now they're inside your house. Stay alive in your bedroom until sunrise to survive. they will activitly search for blUd. movement will increase his awareness ")
print("everytime you open the flashlight their awarness will increase. if you keep hiding in your closet, it has a higher chance the pone ring which increase the chance of them comin")
print("Frequently check each camera to spot them")
choice = int(input("Where would you like to check? :Doorway(1): :Closet(2): :Under your bed(3):     "))
if choice == "1":
    if animatronic == True:
        input("aaahhh quick use flashlight ")
    elif animatronic == False:
        input("nothing here. go back? (Y/N)")



while animatronic == True:
    start = time.time()
    while True:
        elapsed = time.time() 
        
        if elapsed >= 10:
            break


        time.sleep(0.1)

    print("\nStopped after 10 seconds.")

