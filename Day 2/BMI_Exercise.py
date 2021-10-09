# 🚨 Don't change the code below 👇
from turtle import width


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
print(type(height))
print(type(weight))

h_value = float(height)
w_value = int(weight)

#print(type(h_value))
#print(type(w_value))

#print(int(h_value))

#Write your code below this line 
#result = w_value / (h_value * h_value)
result = int(weight) / float(h_value ** 2)

print(result)
print(int(result))