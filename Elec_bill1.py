units = int(input("Enter Units Consumed: "))

if units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)

else:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

total = bill + 100

print("\n----- Electricity Bill -----")
print("Units Consumed   =>", units)
print("Bill Amount      =>", bill)
print("Fixed Charge     => 100")
print("Total Bill       =>", total)


'''
#Mathmatical formulla

If Units ≤ 100
    Bill = Units × 1.50

If Units > 100 and Units ≤ 200
    Bill = (100 × 1.50) + (Units - 100) × 2.50

If Units > 200
    Bill = (100 × 1.50) + (100 × 2.50) + (Units - 200) × 4.00

Total Bill = Bill + 100'''