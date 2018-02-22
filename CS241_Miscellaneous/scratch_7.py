def sort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            print(alist)
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue
        print(alist)
    print(alist)

numbers = [5,3,9,24,13,21]

sort(numbers)