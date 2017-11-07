# File: chaos2point0.py
# A simple program illustrating chaotic behavior. Uses 2.0 instead of 3.9 
# original chaos.py script.
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1-x)
        print(x)
main()
