units = int(input("Enter Units Consumed: "))

rate = 7.5            # Rate per unit (₹)
fixed_charge = 100    # Fixed Charges (₹)
fpppa = 50            # FPPPA Charges (₹)

energy_charge = units * rate
government_duty = energy_charge * 0.05

total_bill = fixed_charge + energy_charge + fpppa + government_duty

print("\n------ Electricity Bill ------")
print("Units Consumed  =>", units)
print("Rate Per Unit   =>", rate)
print("Energy Charges  =>", energy_charge)
print("Fixed Charges   =>", fixed_charge)
print("FPPPA Charges   =>", fpppa)
print("Government Duty =>", government_duty)
print("-------------------------------")
print("Total Bill      =>", total_bill)