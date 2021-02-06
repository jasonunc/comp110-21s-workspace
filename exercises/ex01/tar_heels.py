"""An exercise in remainders and boolean logic."""

__author__ = "730395373"


# Begin your solution here...
unc: int = int(input("Enter an int: "))
if unc%2 == 0 and unc%7 == 0:
    print("TAR HEELS")
else:
    if unc%2 == 0:
        print("TAR")
    else:
        if unc%7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")