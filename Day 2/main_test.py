two_digit_number = input("Type a two digit number: ")

print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit) 

print(result)

#value_1 = int(two_digit_number[0])
#value_2 = int(two_digit_number[1])

#print(value_1 + value_2)

#Mathematical Operations
2 ** 2 # 2 to the power of
2 ** 3

#Order of Oeprations
#()
#**
# * /
#+ -

#Number Manipulation and F Strings

print(round(2.66666,2)) #result 2,67

#Imprime o resultado automaticamente como Integer
print(8 // 3)

restul = 4 / 2 
result /= 2 #Resultado a Dividir por 2
result += 2 #Somar o valor de Result mais 2

#F STRINGS - COmbinar varios tipos para imprimit sem fazer conversão
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")