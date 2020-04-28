colorlist = ["RED", "WHITE", "BLUE", "GREEN", "YELLOW", "PURPLE", "ORANGE", ]
x = 1
color = "start"

def showTitle():
    print("Color Preference Evaluator")

def promptforcolor():
    global color
    color = input("Please type the name of a color\n")
    color = color.upper()
    color = color.strip()
    return color

def confirmcolor():
    global color
    global x
    confirm  = input("You entered {}. Is this correct (Y/N)?\n".format(color))
    confirm = confirm.upper()
    confirm = confirm.strip()
    if confirm == "Y":
        x = 0
        return True
    elif confirm == "N":
        return False

def containselement():
    global color
    if color in colorlist:
        return True
    else:
        return False

def praiseUser():
    global color
    print("Good choice! {} is a cool color.".format(color))

def ridiculeUser():
    global color
    print("Gross, what kind of color is {}?!".format(color))

def main():
    showTitle()
    global x
    global color
    while x == 1:
        promptforcolor()
        confirmcolor()
    if containselement():
        praiseUser()
    else:
        ridiculeUser()
        
    
                                 
main()
