from worker import worker
from CEO import CEO

def print_authors():
    print("//////////////////////////////////////")
    print("/// id:  308542141                ////")
    print("/// name: Elad Natan              ////")
    print("/// mail: elad.glx@email.com      ////")
    print("//////////////////////////////////////")
    print("/// id:   207930868               ////")
    print("/// name: Ofir Goldstein          ////")
    print("/// mail: goldsteinofir@gmail.com ////")
    print("//////////////////////////////////////")

Organization_tree= []




def print_org():
    for root in Organization_tree:
        root.print_manager(3)



def add_employee():
    """
    k_worker_type.print_worker_type_list()
    ui_type = int(input("please enter number to choos the worker type: "))
    type = k_worker_type(ui_type).name
    """

    def run(name, department, age, type, manager_id ):
        if type != 'CEO':
            for employee in Organization_tree:
                tmp = employee.serch_manager(manager_id)
                if tmp != False:
                    tmp.add_employee(worker(name  = name, department = department, age = age,type = type,manager_id = manager_id))
                else:
                    print("manager not exist")
        else:
            Organization_tree.append(CEO(name, department, age))


    run(name="ITZIK_manc", department="nagarot", age=10, type="CEO",manager_id=1)
    run(name="ITZIK2", department="nagarot", age=10, type="CTO", manager_id=1)
    run(name="ITZIK_not", department="nagarot", age=10, type="CEO",manager_id=1)
    run(name="ITZIK3", department="nagarot", age=10, type="CTO", manager_id=2)
    run(name="ITZIK4", department="nagarot", age=10, type="CTO", manager_id=2)
    run(name="ITZIK6", department="nagarot", age=10, type="CTO", manager_id=3)

    print_org()

add_employee()


"""
def run():
    while True:
        command = input("Please enter a command: ")

        if command == "welcome":

            # Receive price
            price = float(input("Please insert the price of the milk:"))

            # Receive expiration date
            exp_date = input("Please insert the expiration date of the milk:")

            # Create a new Milk object, and add it to the <grocery_store> list.
            milk = Milk(price=price, expiration_date=exp_date)
            grocery_store.append(milk)

            total_price += milk.get_price()

        elif command == "add_pepper":
            # Receive color from the user
            color = input("Please insert the color of the pepper:")

            # Receive price_per_kg from the user
            price = float(input("Please insert the pepper's price per KG:"))

            # Receive weight from the user
            weight = float(input("Please insert the pepper's weight:"))

            # Create a new Pepper object, and add it to the <grocery_store> list.
            pepper = Pepper(color=color, price_per_kg=price, weight=weight)
            grocery_store.append(pepper)

            total_price += pepper.get_price()

        elif command == "print":

            # Prints all the items in the <grocery_store> list, using the "print_details" method.
            for item in grocery_store:
                item.print_details()

        elif command == "put_on_shelf":

            # Receives shelf_id from the user
            shelf_id = int(input("Please insert the shelf id:"))

            # Call `put_on_shelf` method with the received <shelf_id> for all the items in the list.
            for item in grocery_store:
                item.put_on_shelf(shelf_id=shelf_id)

        elif command == "total_value":

            # Prints the TOTAL price of all the items in the <grocery_store> list.
            print(f"The total price is {total_price}.")

        elif command == "avg_value":

            # Prints the AVERAGE price of all the items in the <grocery_store> list.
            if len(grocery_store) == 0:
                print(f"No items in the store.")
            else:
                print(f"The average price is {(total_price / len(grocery_store)):.2f}.")

        elif command == "remove":
            is_id_in_grocery_store = False

            # Receive the id of the item to remove from the user
            item_id = int(input("Please insert the id of the item you want to remove:"))

            # if item if exist remove it if not print propper messege
            for item in grocery_store:
                if item.get_id() == item_id:
                    total_price -= item.get_price()  # update total price
                    grocery_store.remove(item)
                    is_id_in_grocery_store = True  # set flag for the print later
                    print(f"Item #{item_id} was removed from the list.")
                    break

            if not is_id_in_grocery_store:
                print(f"Item #{item_id} was not found in the list.")

        elif command == "exit":
            break
        else:
            print(f"Sorry! The command {command} is unknown. Please try again.")

    print("Thank you for using FUN in the GROCERY STORE!")




    e1 = CEO(name="ITZIK", department="nagarot", age=10, type="CEO")
    e5 = worker(name="ITZIK5", department="nagarot", age=10, type="CTO", manager_id=e1.get_id())
    e2 = CEO(name="ITZIK2", department="nagarot", age=10, type="CEO")
    e3 = worker(name="ITZIK3", department="nagarot", age=10, type="CTO", manager_id=e1.get_id())
    e4 = worker(name="ITZIK4", department="nagarot", age=10, type="CTO", manager_id=e3.get_id())
    e6 = worker(name="ITZIK6", department="nagarot", age=10, type="CTO", manager_id=e2.get_id())

    print(e1.get_detail())
    print("/////////////////////////////////////////")
    print(e2.get_detail())
    print("/////////////////////////////////////////")
    print(e3.get_detail())
    print("/////////////////////////////////////////")
    print(e4.get_detail())
    print("/////////////////////////////////////////")
    print(e5.get_detail())
    print("/////////////////////////////////////////")
    print(e6.get_detail())


    e1  = employee(name ="ITZIK", department= "nagarot", age = 10, type = 'CEO')
    ceo = CEO(employee = e1)
    e2  = employee(name ="ITZIK2", department= "nagarot", age = 10, type = 'CTO' )
    cto = worker(employee = e2, manager_id=ceo.get_id())
    e3  = employee(name ="RAMI", department= "nagarot", age = 10, type = 'CEO' )
    ceo3 = CEO(employee = e3)
    e4  = employee(name ="ITZIK4", department= "nagarot", age = 10, type = 'CTO')
    cto4 = worker(employee = e4, manager_id=ceo.get_id())
    print(ceo.get_detail())
    print("/////////////////////////////////////////")
    print(cto.get_detail())
    print("/////////////////////////////////////////")
    print(ceo3.get_detail())
    print("/////////////////////////////////////////")
    print(cto4.get_detail())

"""