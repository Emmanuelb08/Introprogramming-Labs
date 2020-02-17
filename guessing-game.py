def main():
    print("Welcome to Emmanuel's Guessing Game!")
    a = "giraffe"
    x=0
    while x == 0:
        print("I am thinking of an animal...")
        r = str(input("Can you guess what it is?\n"))
        if a==r:
            x=1
            print("Congragulations! You've guessed it.")
        else:
            print("Sorry, that is incorrect. Please try again!")

main()
                
        
        
        
