def pair_sum(numlist, k): 
    solutions = []
    for i in numlist:
        print(numlist.index(i), i)
        target  = k - i 
        if target in numlist: 
            solutions.append([i,target])
            numlist.remove(i)
            numlist.remove(target)
            print(f"i: {numlist}, removed {i} and {target}")

    
    if solutions == []: 
        print("No sum pairs found for k in numlist.")
    else: print(f"sum pairs in numlist: {solutions}")
    print("numlist:",numlist)

def main(): 
    return pair_sum([6,1,3,2,2,2,2,3,1,4,0], 4)
if __name__ == "__main__":
    main()