import sys

def add(num1,num2):
    return int(num1) + int(num2)

def sub(num1, num2):
    return int(num1) - int(num2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("You need to pass two integers to run this module")
        exit(1)
    n1,n2 = sys.argv[1:]
    print(f"The sum is {add(n1,n2)}")
    print(f"The difference is {sub(n1,n2)}")
