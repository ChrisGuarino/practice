def anagram(s1,s2): 
    #Normalize the inputs 
    s1_norm = s1.lower().replace(" ","")
    s2_norm = s2.lower().replace(" ","")
    
    if len(s1_norm) == len(s2_norm): 
        print("Same length")
        for i in s1_norm: 
            if i in s2_norm: 
                s1_norm.replace(i,"")
                s2_norm.replace(s2_norm[s2_norm.index(i)],"")
            else: 
                print(f"Not an anagram. {i} is not in {s2}")
            
        print(f"Anagram detected: {s1} is an anagram with {s2}")
    else: print("Length mismatch!")
        
def main(): 
    return anagram("go go go", "gggooo")

if __name__ == "__main__":
    main()