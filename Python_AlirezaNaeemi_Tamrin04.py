# Python_AlirezaNaeemi_Tamrin04

salary = float(input("Hoghogh mahane ra vared konid (toman): "))
has_child = input("Aya karmand farzand darad? (y/n): ").strip().lower() == "y"

if salary <= 10_000_000:
    tax = 0.0
elif salary <= 25_000_000:
    tax = (salary - 10_000_000) * 0.10
else:
    tax_first_bracket = (25_000_000 - 10_000_000) * 0.10
    tax_second_bracket = (salary - 25_000_000) * 0.20
    tax = tax_first_bracket + tax_second_bracket

if has_child:
    tax -= 500_000
    if tax < 0:
        tax = 0.0

net_salary = salary - tax

print("\n--- Report maliat va hoghogh ---")
print(f"Hoghogh nakhales : {salary:,.0f} toman")
print(f"Maliat nahayi    : {tax:,.0f} toman")
print(f"Hoghogh khales   : {net_salary:,.0f} toman")