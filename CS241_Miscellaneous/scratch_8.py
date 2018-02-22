numlist = [3,12,4,7,1]


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    sublist = [numbers[0]]
    for i in range(len(numbers)-1):
        print("iteration i={}".format(i))
        print("sublist: ", sublist)
        sublist.append("x")
        print("sublist: ", sublist)
        for k in range(i,-1,-1):
            print(" for k={}".format(k,i))
            print("  check sublist[k] = {} > numbers[i+1] = {}:".format(sublist[k], numbers[i+1]))
            if sublist[k] > numbers[i+1]:
                print("   TRUE: assign sublist[k+1] = {} <- sublist[k] = {}".format(sublist[k+1], sublist[k]))
                sublist[k+1] = sublist[k]
                sublist[k] = "x"
                if sublist[0] == "x":
                    sublist[0] = numbers[i+1]
                print("    sublist: ", sublist)
            else:
                print("   FALSE: assign sublist[k+1] = {} <- numbers[i+1] = {}".format(sublist[k+1], numbers[i+1]))
                sublist[k+1] = numbers[i+1]
                print("    sublist: ", sublist)
                break

    numbers = sublist

sort(numlist)
print(numlist)
