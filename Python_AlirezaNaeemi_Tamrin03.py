#Python_AlirezaNaeemi_Tamrin03

monthly_salary = float(input("Hoghogh mahane ra vared konid: "))

tax_rate = 0.10
tax_amount = monthly_salary * tax_rate
net_salary = monthly_salary - tax_amount

print("\n--- Natije mohasebe hoghogh va maliat ---")
print(f"Hoghogh mahane : {monthly_salary:,.2f}")
print(f"Maliat (10%)   : {tax_amount:,.2f}")
print(f"Hoghogh khales : {net_salary:,.2f}")