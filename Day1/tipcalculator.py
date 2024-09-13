#tip calculator

print("Welcome to the Tip Collector")
bill  = float(input("What is the Bill? $"))
num = int(input("How many will go Dutch and Pay the Bill? ")) #dutch means paying 50/50
tip = int(input("What will be your Tip percentage? 5, 10, 12, 15  Tip%: "))

#bill each person
bill_each = float((bill/num))

#tip each person
tip_each =float(1+(tip/100))
total_bill_each = round(bill_each*tip_each,3)

print(f"Each Person will pay ${total_bill_each}.") 