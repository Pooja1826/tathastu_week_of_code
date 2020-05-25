N=int(input("Enter the value of N:"))
a=0
b=1
print('Fibonacci seriesn upto',N,'is : ')
for i in range(N) : 
    print(a," ")
    c=a+b
    a=b
    b=c
