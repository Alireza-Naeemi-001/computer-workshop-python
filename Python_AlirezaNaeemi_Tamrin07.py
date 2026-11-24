# Python_AlirezaNaeemi_Tamrin07

inventory = {
    "Chips": {"price": 25_000, "stock": 12},
    "Pofak": {"price": 15_000, "stock": 3},
    "Chocolate": {"price": 40_000, "stock": 2},
}

LOW_STOCK_THRESHOLD = 5

while True:
    print("\n=== System Modiriyat Anbar ===")
    print("1. Add & Save kardan kala ya update mojoodi")
    print("2. Sabt forosh")
    print("3. Kalaye ro be etmam")
    print("4. Arzesh riyali anbar")
    print("5. Namayesh kalahaye anbar")
    print("6. Exit")

    choice = input("Gozine mored nazar ra entekhab konid (1 ta 6): ").strip()

    if choice == "1":
        item_name = input("Name kala: ").strip()
        price = int(input("Price (rial): "))
        quantity = int(input("Tedad mojodi baraye ezafe shodan: "))

        if price < 0 or quantity < 0:
            print("Price va tedad nemitavanand manfi(-x) bashand.")
            continue

        if item_name in inventory:
            inventory[item_name]["price"] = price
            inventory[item_name]["stock"] += quantity
            print(f"Kalaye '{item_name}' update shod. Mojodi jadid: {inventory[item_name]['stock']}")
        else:
            inventory[item_name] = {"price": price, "stock": quantity}
            print(f"Kalaye jadid '{item_name}' dar anbar sabt shod.")

    elif choice == "2":
        item_name = input("Name kalaye forookhte shode: ").strip()
        if item_name not in inventory:
            print(f"Kalayi ba name '{item_name}' dar anbar vojod nadarad.")
            continue

        sold_qty = int(input("Tedad forokhte shode: "))
        current_stock = inventory[item_name]["stock"]

        if sold_qty <= 0:
            print("Tedad forosh bayad bozorgtar az 0 bashad.")
        elif sold_qty > current_stock:
            print(f"Mojodi kafi nist! Mojoodi '{item_name}': {current_stock}")
        else:
            inventory[item_name]["stock"] -= sold_qty
            sale_total = sold_qty * inventory[item_name]["price"]
            print(f"Forosh sabt shod. total sale : {sale_total:,} rial | Mojoodi baghimande: {inventory[item_name]['stock']}")

    elif choice == "3":
        print(f"\n--- kalaye ro be etmam (kochiktar mosavi {LOW_STOCK_THRESHOLD} adad) ---")
        low_items = {
            name: info for name, info in inventory.items()
            if info["stock"] <= LOW_STOCK_THRESHOLD
        }

        if not low_items:
            print("Hich kalayi dar vaziyat ro be etmam nist.")
        else:
            for name, info in low_items.items():
                print(f"- {name}: {info['stock']} adad baghimande (price: {info['price']:,} rial)")

    elif choice == "4":
        total_value = sum(info["price"] * info["stock"] for info in inventory.values())
        print(f"\nKole mojodi riyali anbar: {total_value:,} rial")

    elif choice == "5":
        if not inventory:
            print("Anbar khali ast.")
        else:
            print("\n--- List anbar ---")
            for name, info in inventory.items():
                item_total = info["price"] * info["stock"]
                print(f"- {name} | Price: {info['price']:,} rial | Mojodi: {info['stock']} | Arzesh: {item_total:,} rial")

    elif choice == "6":
        print("Exiting modiriyat anbar...")
        break

    else:
        print("Error! adadi beyn 1 ta 6 vared konid.")