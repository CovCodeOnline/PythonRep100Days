#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")

bill_value = float(input("What was the total bill? $"))
print(type(bill_value))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
print(type(percentage_tip))

number_of_people = int(input("How many people to split the bill? "))

tip_as_percentage = percentage_tip / 100

total_tip_amount = bill_value * tip_as_percentage

total_bill = bill_value + total_tip_amount
#print(bill_value)
#print(number_of_people)
bill_per_person = total_bill / number_of_people
#print(people_value)
final_value = round(bill_per_person,2)

#coloca um 0 quando falta nas casas decimais 33.2 passa a 33.20
final_value = "{:.2f}".format(bill_per_person)

print(f"Each Person should pay: ${final_value}")