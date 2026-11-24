# Python_AlirezaNaeemi_Tamrin06

watchlist = []

while True:
    print("\n=== Watchlist ===")
    print("1. Add film")
    print("2. Delete film")
    print("3. Mortab sazi film ha(alphabet)")
    print("4. Namayesh list tamasha")
    print("5. Exit")

    choice = input("Gozine mored nazar ra vared konid (1 ta 5): ").strip()

    if choice == "1":
        name = input("Name film ra vared konid: ").strip()
        year = int(input("Tarikh enteshar ra vared konid(Year): "))
        rating = float(input("Emtiyaz film ra vared konid (X.X): "))

        movie = (name, year, rating)
        watchlist.append(movie)
        print(f"Film '{name}' ba movafaghiyat be list ezafe shod.")

    elif choice == "2":
        target_name = input("Name filmi ke mikhahid hazf konid ra vared konid: ").strip()
        found_index = -1

        for i in range(len(watchlist)):
            if watchlist[i][0].lower() == target_name.lower():
                found_index = i
                break

        if found_index != -1:
            removed_movie = watchlist.pop(found_index)
            print(f"Film '{removed_movie[0]}' az list hazf shod.")
        else:
            print(f"Filmi ba name '{target_name}' dar list peyda nashod.")

    elif choice == "3":
        watchlist.sort(key=lambda movie: movie[0].lower())
        print("List film ha be soorat alphabet mortab shod.")

    elif choice == "4":
        if not watchlist:
            print("List tamashaye shoma khali ast.")
        else:
            print("\n--- Film haye mojod dar Watchlist ---")
            for idx, (name, year, rating) in enumerate(watchlist, start=1):
                print(f"{idx}. {name} ({year}) | Emtiyaz: {rating}")

    elif choice == "5":
        print("Exiting Watchlist...")
        break

    else:
        print("Error! adadi beyn 1 ta 5 vared konid.")