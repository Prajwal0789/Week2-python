Num=int(input("Enter the size of Array"))
N=0
maxcount=0
A=[]
for i in range (0,Num):
    A.append(int(input(f"enter the {i+1} element")))

print("The elements of the array are: ")
for ele in A:
    print(ele)

for i in range(Num):
    count=0
    for j in range(Num):
        if A[i]==A[j]:
            count+=1
    if A[i]!=N and count>maxcount:
        num=A[i]
        maxcount=count

print("The number wiht max apperance is :" +str(num))
print("Count=",maxcount)

