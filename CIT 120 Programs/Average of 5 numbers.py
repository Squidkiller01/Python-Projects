#Complicated average of 5 numbers
import statistics

num = []
MIN = 0
MAX = 100
p=0
exit = 0
while exit != 1:    
    while p < 5:
        try:
            x = float(input("Input a number: "))
            if x >= MIN or x <= MAX:
                num.append(x)
                p += 1
        except ValueError:
            print("That wasn't a number!")
    print(*num, sep = ", ")
    print(str(statistics.mean(num)))
    try:    
        option = input("Would you like to exit the program?")
        if option == "Yes" or option == "yes":
            exit = 1
            exit
        elif option != "Yes" or option != "yes" or option != "No" or option != "no":
            print("That was not an option!")
    except ValueError:
        print("That wasn't a word!")