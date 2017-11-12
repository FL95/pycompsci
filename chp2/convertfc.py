#convertfc.py
#    A program to convert Fahrenheit temps to Celsius
# Example from Python Programming: An Introduction to Computer Science by John Zelle

def main():
    print("This program converts Fahrenheit temperatures to Celsius.")
    
    fahrenheit = eval(input("What is the Fahrenheit temperature?"))
    celcius = (fahrenheit - 32) * 5/9
    print("The temperature is", celcius, "degrees Celsius")

    input("Press the <Enter> key to quit.")

main()
