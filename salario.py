number = input()
hours_worked = input()
v_hour = input()

hours_worked = float(hours_worked)
v_hour = float(v_hour)

salary = hours_worked * v_hour

print("NUMBER = " + number)
print(f"SALARY = U$ {salary:.2f}")
