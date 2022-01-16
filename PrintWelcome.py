def printWelcome(name, times):
    for i in range(0, times):
        print("Welcome" + name + " ", end="")


name = input("Please type your name: ")
times = int(input("How many times: "))
printWelcome(name.capitalize().times)
