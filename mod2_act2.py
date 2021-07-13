# mod2_act2.py

"""
Tasks
1. Write a program code that allows the user to input values for a
    salesperson's base salary, total sales, and commission rate. The
    program calculates and displays the salesperson's pay by adding
    the base salary to the product of the total sales and
    commission rate.
"""

base_salary = float(input("Base salary: "))
total_sales = float(input("Total sales: "))
commission_rate = float(input("Commission rate: "))

salesperson_pay = base_salary + (total_sales * commission_rate)
print("Salesperson's pay: {:.2f}".format(salesperson_pay))
