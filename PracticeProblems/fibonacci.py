pos=int(input("Enter position:"))

one=0
two=1

if(pos==0):
    print(one)
if(pos==1):
    print(two)

for i in range(pos-1):
    one,two=two,two+one
print(two)