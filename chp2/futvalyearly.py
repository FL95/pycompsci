# futvalyearly.py
#    Future value of an amount invested yearly

def main():
    print("This program calculates the future value of an investment")
    print()

    payment = eval(input("Enter amount to invest each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))

    principal = 0.0
    for i in range(years):
        principal = (principal + payment) * (1 + apr)


    print("The value in ", years, "years is: ", principal)

main()