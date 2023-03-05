#Найдите сумму цифр трехзначного числа.

a = int(input())
sum = 0 
while a > 0:
     c = a % 10
     sum = sum + c
     a = a//10
print("cсумма чисел", sum)





