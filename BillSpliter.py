# Python implementation here
print("Welcome To The Bill Spliter")

total_bill = float(input("What is the total bill?: "))

percentage_tip = int(input("What % tip would you like to give?: "))

number_of_people = int(input("How many people are splitting the bill?: "))
print("\n")

payment_per_person = ("%.2f" % round(float(((percentage_tip / 100 +1) * total_bill) / number_of_people), 2))

tip_amount = "%.2f" % float(percentage_tip / 100 * total_bill)
print(f"Tip amount: Rs{tip_amount}")

total_bill_float = float(total_bill)
tip_amount_float = float(tip_amount)
tip_and_total = (total_bill_float+tip_amount_float)
print(f"Total bill including tip: Rs{tip_and_total}")
#Print what each person needs to pay
print(f"Each person owes: Rs{payment_per_person}")