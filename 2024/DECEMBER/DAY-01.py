#--------------------------------------------------------------------------------------------------
#PART - ONE
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-1.1.txt", "r") as input:
    
    arr1 = []
    arr2 = []
    t = 0
    
    for line in input:
        l, r = line.split()
        arr1.append(l)
        arr2.append(r)
        
    arr1.sort()
    arr2.sort()

    for i in range(len(arr1)):
        t += abs(int(arr1[i]) - int(arr2[i]))
        
    print(t)
#--------------------------------------------------------------------------------------------------
#PART - TWO
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-1.2.txt", "r") as input2:
    
    al1 = []
    al2 = []
    tot = 0
    
    for line in input2.readlines():
        l, r = line.split()
        al1.append(int(l))
        al2.append(int(r))
    
    for i in al1:
        tot += i * al2.count(i)
    
    print(tot)
#--------------------------------------------------------------------------------------------------