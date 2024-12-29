#--------------------------------------------------------------------------------------------------
#PART - ONE
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-5.1.txt", 'r') as inputs:

    rules, updts = inputs.read().split("\n\n")
    rules = rules.split()
    updts = [list(map(int, update.split(','))) for update in updts.splitlines()]

    res = []
    total = 0

    for i in updts:
        for j in rules:
            num1, num2 = j.split("|")
            num1 = int(num1)
            num2 = int(num2)
            check = True
            if num1 in i and num2 in i:
                if i.index(num1) > i.index(num2):
                    check = False
                    break
        if check == True:
            res.append(i)

    for arr in res:
        n = len(arr)//2
        total += int(arr[n])

    print("PART - ONE : " + str(total))
#--------------------------------------------------------------------------------------------------
#PART - TWO
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-5.1.txt") as sample:
    
    sample = sample.read()

    rules2, updts2 = sample.split("\n\n")
    rules2 = rules2.split()
    updts2 = [list(map(int, update.split(','))) for update in updts2.splitlines()]

    edited = []
    total2 = 0

    def sort_update(update, rules2):
        sorted_update = update[:]
        for _ in range(len(update)):
            for j in rules2:
                nums1, nums2 = j.split("|")
                nums1 = int(nums1)
                nums2 = int(nums2)
                if nums1 in sorted_update and nums2 in sorted_update:
                    if sorted_update.index(nums1) > sorted_update.index(nums2):
                        idx1, idx2 = sorted_update.index(nums1), sorted_update.index(nums2)
                        sorted_update[idx1], sorted_update[idx2] = sorted_update[idx2], sorted_update[idx1]
        return sorted_update

    for i in updts2:
        check2 = True
        for j in rules2:
            nums1, nums2 = j.split("|")
            nums1 = int(nums1)
            nums2 = int(nums2)
            if nums1 in i and nums2 in i:
                if i.index(nums1) > i.index(nums2):
                    check2 = False
                    break
        if check2 == False:
            sorted_i = sort_update(i, rules2)
            edited.append(sorted_i)

    for arr in edited:
        n = len(arr)//2
        total2 += int(arr[n])

    print("PART - TWO : " + str(total2))
#--------------------------------------------------------------------------------------------------