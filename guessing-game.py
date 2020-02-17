def main():
    print("Welcome to Emmanuel's Guessing Game!")
    a = "giraffe"
    x=0
    q = "quit"
    while x == 0:
        print("I am thinking of an animal...")
        r = str(input("Can you guess what it is?\n"))
        r = r.lower()
        if r[0] == "q":
            x=1
            print("No one likes a quitter. Come back soon!")
        elif a==r:
            x=1
            print("Congragulations! You've guessed it.")
            like=input("Do you like {}'s?".format(a))
            if like[0] == "y":
                print("They're just the coolest, aren't they!")
            elif like[0] == "n":
                print("Why not? They're awesome!?")
        else:
            print("Sorry, that is incorrect. You can type quit to give up. Please try again!")

main()
                
        
        
        

