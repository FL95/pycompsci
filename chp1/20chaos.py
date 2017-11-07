# File: 20chaos.py
# A simple program illustrating chaotic behavior. Loops 20 times instead 
# of original script's 10 times.
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1-x)
        print(x)
main()
