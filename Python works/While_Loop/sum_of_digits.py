# read a number and print sum of digits


num=int(input("Enter a number "))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)