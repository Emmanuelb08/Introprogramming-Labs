def main():
    print("Welcome to Emmanuel's Guessing Game!")
    a = "giraffe"
    x=0
    q = "quit"
    while x == 0:
        print("I am thinking of an animal...")
        r = str(input("Can you guess what it is?\n"))
        r = r.lower()
        if a==r:
            x=1
            print("Congragulations! You've guessed it.")
        elif r==q:
            x=1
            print("No one likes a quitter. Come back soon!")
        else:
            print("Sorry, that is incorrect. You can type quit to give up. Please try again!")

main()
                
        
        
        

