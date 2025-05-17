name = input()
salary = float(input())
total_sales = float(input())


commission = total_sales * 0.15
total_salary = commission + salary

print(f"TOTAL = R$ {total_salary:.2f}")
