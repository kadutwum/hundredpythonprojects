
# Obtain User inputs 
item_1 = input("what is the first item in your basket? ")
price_1 = float(input("what is the price of this? "))
item_2 = input("what is the second item in your basket? ")
price_2 = float(input("what is the price of this? " ))
item_3 = input("what is the third item in your basket? ")
price_3 = float(input("what is the price of this? "))
total = price_1 + price_2 + price_3

# declare the static components of the receipt
message ="Thank for shopping with us."
address_name = "Python Academy, Inc."
address_street = "1502 Somewhere Ave."
address_city = "CityName, State"

# print out receipt
print("*" * 50)
print("\t\t{}\n\t\t{}\n\t\t{}".format(address_name, address_street, address_city))#using string.format() to output company name and address
print("=" * 50)
print("\tProduct Name\t\tProduct Type")
print("\t{}\t\t\t{}".format(item_1, price_1)) #print(item_1 + "\t\t\t $"+ str(price_1)) will produce the same output
print("\t{}\t\t\t{}".format(item_2, price_2))
print("\t{}\t\t\t{}".format(item_3, price_3))
print("=" * 50)
print("\t\t\t\tTotal")
print("\t\t\t\t${}".format(total))
print("=" * 50)
print("\t\t{}".format(message))
print("*" * 50)
