# Header
print("Hello, I am your tip calculator \n")

# Taking the total for the bill
total_bill = input("What was the total for the bill? \n£")

# Taking how many people to split the bill between
group_size = input("How many people is the bill being split between? \n")

# Taking how much you want to tip
tip_percentage = input("What percentage tip would you like to give?: 10, 12, or 15 \n")

# Calculating how much each person will pay without tip included
per_person_bill = (float(total_bill) / float(group_size)) 

# Calculating tip
tip = per_person_bill * float(tip_percentage) / 100

# Adding tip to to total amount to pay per person
total_per_person = "{:.2f}".format(per_person_bill + tip)

# Printing outcome
print(f"Each person should pay: £{total_per_person}")