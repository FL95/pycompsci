# futval.py
#    A program to compute the value of an investment
#    carried x number of years into the future

def main():
    print("This program calculates the future value of an investment")
    print()

    principal = eval(input("Enter the initial principle: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)


    print("The value in ", years, "years is: ", principal)

main()