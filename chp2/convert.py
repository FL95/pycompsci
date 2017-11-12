#convert.py
#    A program to convert Celsius temps to Fahrenheit
# Example from Python Programming: An Introduction to Computer Science by John Zelle

def main():
    print("This program converts Celsius temperatures to Fahrenheit.")
    
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature?"))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit")

    input("Press the <Enter> key to quit.")

main()
