# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
number_age = 90 - int(age)
#Write your code below this line 👇
num_days = int(number_age) * 365
num_weeks = int(number_age) * 52
num_months = int(number_age) * 12

message = f"You have {num_days} days, {num_weeks} weeks and {num_months} months left."

print(message)