
numbers=[1,2,[3,[100,200,300],4],5,6]

print(numbers[2])           # [3,[100,200,300],4]
print(numbers[2][1])        # [100,200,300]

numbers[2][1].append(500)   # [100,200,300,500]
print(numbers)              # [1,2,[3,[100,200,300,500],4],5,6]
