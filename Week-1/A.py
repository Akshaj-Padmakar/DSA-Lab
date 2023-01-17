import array as arr
from itertools import permutations

a = arr.array('i' ,[200108005, 200108011, 200108061])



l = list(permutations(a))

print("Q1. These are the permutations")
for i in range(0,6):
    print(l[i])

mean = 0;

for  i in a:
    z = str(i)
    for x in z :
        mean += int(x)

mean/= 27;
roundMean = int(mean)

print("\n")
print("Q2. The mean of all the digits is " + str(mean) + " and after rounding-off, it comes out to be " + str(roundMean))
print("\n")


for i in range(0,6):
    print("Q3. For permutation " + str(i+1) + ", the indices at which " + str(roundMean) + " is present are ")
    for y in range(0,3):
        z = str(l[i][y])
        for x in range(0,9):
            if(int(z[x]) == roundMean):
                print(str(y*9 + x))



aa = [2,0,0,1,0,8,0,0,5,2,0,0,1,0,8,0,1,1,2,0,0,1,0,8,0,6,1]


aa.sort()
print("\n")
print("Q4. After sorting: ")
for x in aa:
    print(x)


l = 0
r = 27


while (r-l>1):
    md = int((r+l)/2)
    

    if(aa[md]==roundMean):
        r = md
    elif(aa[md]>roundMean):
        r = md-1
    else:
        l = md+1
print("\n")
print("Q5. Using B.S.A., we get the indices with " + str(roundMean) + " are")
for i in range(r,27):
    if(aa[i]!=roundMean):
        break
    print(i)
