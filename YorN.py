ch = "y"
while ch not in ["n", "N", "no", "No"]:
        ch = input("Enter Y to continue or N to exit: ")
        if ch not in ["n","N", "no", "No", "y", "Y", "yes", "Yes"]:
           print("Enter only Y or N")
