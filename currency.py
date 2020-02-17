value_dollar = int(input("Please enter a dollar value: "))
value_rupee = int(input("Please enter a rupee value: "))

d = round(value_rupee / 70, 2)
r = round(value_dollar * 70, 2)

print("The equivalent of", value_dollar, "dollars" ,"is", r, "rupees")
print("The equivalent of", value_rupee, "rupees" ,"is", d, "dollars")