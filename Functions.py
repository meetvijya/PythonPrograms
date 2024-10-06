# Function within function and Passing Function as parameter

def DisplayMsg(str):
    def addWelcome():
        return "Welcome to "
    return addWelcome() + str

def site(name):
    return name

print(DisplayMsg(site("Python")))
