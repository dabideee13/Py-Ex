# mod2_act2.py

base_salary = float(input("Base salary: "))
total_sales = float(input("Total sales: "))
commission_rate = float(input("Commission rate: "))

salesperson_pay = base_salary + (total_sales * commission_rate)
print("Salesperson's pay: {:.2f}".format(salesperson_pay))
