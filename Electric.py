# 1.12 Electric Bill Calculator
prev_reading = float(input("Enter previous meter reading: "))
curr_reading = float(input("Enter current meter reading: "))
units_consumed = curr_reading - prev_reading
fixed_charge = 100.0
total_bill = (units_consumed * 5.50) + fixed_charge
print(f"Units Consumed: {units_consumed:.2f}")
print(f"Total Electric Bill: ₹{total_bill:.2f}")prev_reading = float(input("Enter previous meter reading: "))
curr_reading = float(input("Enter current meter reading: "))
units_consumed = curr_reading - prev_reading
fixed_charge = 100.0
total_bill = (units_consumed * 5.50) + fixed_charge
print(f"Units Consumed: {units_consumed:.2f}")
print(f"Total Electric Bill: ₹{total_bill:.2f}")