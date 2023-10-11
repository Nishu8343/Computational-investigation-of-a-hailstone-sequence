num1 = 0
count = 0
max_length = 1

m = int(input("Enter a number: "))
b = int(input("Enter a base number: "))
num = pow(b,m)-1
print("For the value of m, num = ", num)

Max = num
    
while num !=4:
    if num % 2 == 0:
        num = num/2
    else:
        num = 3*num +1
    num1 = int(num)    
    print(num1 , end= " ")
    count += 1
    if Max < num1:
        Max = num1
        max_length = count


   
print("\nMaximum: " , Max)

print("Count: " , count)

print("Max_length: " , max_length)

    

