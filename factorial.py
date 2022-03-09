print('1.Factorial using for loop')
print('2.Factorial using recursion')
ch=input('Enter your choice')
if ch=='1':
    n=int(input("Enter the number you want the factorial: "))
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

elif ch=='2':
    def fact(n):
        if n==1:
            return n
        else:
            return n*fact(n-1)
    num=int(input('Enter the number" '))
    if num<0:
        print('Factorial does not exist')
    elif  num==0:
        print('Fatoiral is equal to 1')
    else:
        print('The factorial is: ',fact(num))
else: 
    print("wrong Choice")