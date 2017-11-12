#ktom.py
#    A program to convert Kilometers to Miles

def main():
    print("This program converts Kilometers to Miles.")
    
    kilometers = eval(input("Enter the number of kilometers: "))
    miles = kilometers * .62

    print("The number of miles is: ", miles)
    input("Press the <Enter> key to quit.")

main()
