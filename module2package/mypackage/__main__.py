import sys
import mypackage.support_functions


if len(sys.argv) != 3:
    print("You need to pass two integers to run this module")
    exit(1)
n1, n2 = sys.argv[1:]
print(f"The sum is {mypackage.support_functions.add(n1,n2)}")
print(f"The difference is {mypackage.support_functions.sub(n1,n2)}")
