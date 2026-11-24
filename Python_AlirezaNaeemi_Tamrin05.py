# Python_AlirezaNaeemi_Tamrin05

balance = 1_000_000

while True:
    print("\n=== Menu ATM ===")
    print("1. Mojoodi")
    print("2. Bardasht")
    print("3. Variz")
    print("4. Exit")

    choice = input("Gozine mored nazar ra entekhab konid (1 ta 4): ").strip()

    if choice == "1":
        print(f"Mojoodi shoma: {balance:,} toman")

    elif choice == "2":
        amount = int(input("Meghdar bardasht ra vared konid (toman): "))
        if amount <= 0:
            print("Meghdar bardasht bayad bozorgtar az 0 bashad.")
        elif amount > balance:
            print(f"Mojodi kafi nist! Mojodi shoma {balance:,} toman")
        else:
            balance -= amount
            print(f"Bardasht Successful. Mojoodi jadid: {balance:,} toman")

    elif choice == "3":
        amount = int(input("Meghdar variz ra vared konid (toman): "))
        if amount <= 0:
            print("Meghdar variz bayad bozorgtar az 0 bashad.")
        else:
            balance += amount
            print(f"Variz Successful. Mojoodi jadid: {balance:,} toman")

    elif choice == "4":
        print("Khorooj az system...")
        break

    else:
        print("Error! adadi beyn 1 ta 4 vared konid.")