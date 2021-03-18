title = "tip calculator"
greetings = "Welcome to the tip calculator"
print("\t\t\t\t\t" + title.upper() + "\n\t\t\t" + greetings + "\n") 
bill = float(input("What is the bill amount?\t"))
number_of_people = int(input("How many people are spliting the bill?\t"))
tip_options = float(input("What percentage of tip would you like to leave? 10, 12, 15?\t"))
tip = bill*(tip_options / 100)
totalbill_per_person = round(((bill + tip) / number_of_people), 2)
print("Each person should pay {}".format(totalbill_per_person))
##
