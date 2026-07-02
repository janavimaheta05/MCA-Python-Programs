units = int(input("Enter Units Consumed: "))

if units <= 100:
    energy_charge = units * 1.5

elif units <= 200:
    energy_charge = (100 * 1.5) + ((units - 100) * 2.5)

else:
    energy_charge = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

# Other Charges
fixed_charge = 100
fpppa = 50
government_duty = energy_charge * 0.05   # 5% of Energy Charge

# Total Bill
total_bill = fixed_charge + energy_charge + fpppa + government_duty

print("\n------ Electricity Bill ------")
print("Units Consumed   => ", units)
print("Energy Charges   => ", energy_charge)
print("Fixed Charges    => ", fixed_charge)
print("FPPPA Charges    => ", fpppa)
print("Government Duty  => ", government_duty)
print("------------------------------")
print("Total Bill       => ", total_bill)


'''
Mathematical Formula

If Units ≤ 100
    Energy Charges = Units × 1.50

If Units > 100 and Units ≤ 200
    Energy Charges = (100 × 1.50) + (Units - 100) × 2.50

If Units > 200
    Energy Charges = (100 × 1.50) + (100 × 2.50) + (Units - 200) × 4.00

Government Duty = 5% of Energy Charges

Total Bill = Fixed Charges + Energy Charges + FPPPA + Government Duty
'''
