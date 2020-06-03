from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
element = int(input("Select an element in the array to check the occurance ")
occ = 0
for i in array_num:
    if i == element:
        occ +=1
print(occ) 