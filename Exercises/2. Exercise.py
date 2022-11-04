'''
1. factorial program
2. odd/ even
3. prime number
4. fibonacci series
5. various patterns
6. sum of all even numbers from 1 to 10
7. sum of all odd numbers from 1 to 10
'''

#5!=1*2*3*4*5
'''number=int(input("Enter the number: "))
#looping
if number==0:
    print("factorial of", number,"=1")
fact=1
for i in range(1,number+1,1):
    fact=fact*i #fact*=i
print(fact)
'''
#multiplication program
'''2X1=2
2X2=4
.
.
.
.
2X10=20'''
'''for j in range(2,11,1):
    for i in range(1,11,1):
        print(j,"X",i,"=",j*i)
    print()'''
'''
0
01
012
0123
01234'''
for i in range(1,5):
    for j in range(i):
        print(j, end="")
    print()
