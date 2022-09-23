import numpy as np
import csv

input1 = input()

# output
print(input1.upper())
out = ""
for i,x in enumerate(input1):
    if (i%2 == 0):
        out += input1[i].lower()
    else:
        out += input1[i].upper()
print (out)
arr = [*input1]
np.savetxt("thecsv.csv",
           arr,
           delimiter =", ",
           fmt ='% s')

print ('CSV created!')
