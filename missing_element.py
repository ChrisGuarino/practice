#compares two lists of ints and finds the element that is missing. 
def finder(list1,list2): 
    #Get Length to confirm they are of different sizes. 
    for ele in list1: 
        if ele not in list2: 
            print(f'"{ele}" is the missing element in list2.')
def main(): 
    return finder([1,3,4,4,6,9], [3,9,6,4,1])

if __name__ == "__main__":
    main()