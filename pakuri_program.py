from pakudex import Pakudex

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    run = True
    cap_max = 0
    while run:
        try:
            cap_max = int(input("Enter max capacity of the Pakudex: "))
            if cap_max < 0:
                raise ValueError
            if cap_max != int(cap_max):
                raise ValueError
            if cap_max > 0:
                run = False
        except ValueError:
            print("Please enter a valid size.")

    print(f"The Pakudex can hold {cap_max} species of Pakuri.\n")
    object = Pakudex(capacity=cap_max)

    refrigerator_running = True
    while refrigerator_running:

        # pakudex = Pakudex(capacity=5)
        # species = "psygoose"
        # pakudex.add_pakuri(species)

        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")
        try:
            option = int(input("\nWhat would you like to do? "))
            if option == 0:
                raise ValueError
            if (option != int(option)) or option > 6 or option < 0:
                raise ValueError

            if option == 1:
                list_pakuri = object.get_species_array()
                if list_pakuri == None:
                    print("No Pakuri in Pakudex yet!\n")
                else:
                    print("Pakuri In Pakudex:")
                    count = 1
                    for species in list_pakuri:
                        print(f"{count}. {species}")
                        count += 1
                    print()

            if option == 2:
                x = input("Enter the name of the species to display: ")
                show_pakuri = object.get_stats(x)
                if show_pakuri == None:
                    print("Error: No such Pakuri!\n")
                else:
                    print(f"\nSpecies: {x}")
                    print(f"Attack: {show_pakuri[0]}")
                    print(f"Defense: {show_pakuri[1]}")
                    print(f"Speed: {show_pakuri[2]}\n")

            if option == 3:
                if object.get_size() == object.get_capacity():
                    print("Error: Pakudex is full!\n")
                else:
                    m = input("Enter the name of the species to add: ")
                    if object.add_pakuri(m) == False:
                        print("Error: Pakudex already contains this species!\n")
                    else:
                        print(f"Pakuri species {m} successfully added!\n")

            if option == 4:
                y = input("Enter the name of the species to evolve: ")
                evolve_pakuri = object.evolve_species(y)
                if evolve_pakuri == True:
                    print(f"{y} has evolved!\n")
                if evolve_pakuri == False:
                    print("Error: No such Pakuri!\n")

            if option == 5:
                object.sort_pakuri()
                print("Pakuri have been sorted!\n")

            if option == 6:
                print("Thanks for using Pakudex! Bye!")
                refrigerator_running = False
        except ValueError:
            print("Unrecognized menu selection!\n")