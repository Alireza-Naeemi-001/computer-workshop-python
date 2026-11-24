# Python_AlirezaNaeemi_Tamrin03.1

num1_str = input("Adad 1 ra vared konid: ")
num2_str = input("Adad 2 ra vared konid: ")

num1 = float(num1_str)
num2 = float(num2_str)

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2

print("\n--- Natije 4 amal asli va noe dade ---")
print(f"Jam      : {sum_result} -> {type(sum_result)}")
print(f"Tafrigh  : {sub_result} -> {type(sub_result)}")
print(f"Zarb     : {mul_result} -> {type(mul_result)}")

if num2 != 0:
    div_result = num1 / num2
    print(f"Taghsim  : {div_result} -> {type(div_result)}")
else:
    print("Taghsim  : taghsim bar 0 momken nist.")