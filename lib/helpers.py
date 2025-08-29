import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'db'))

from db.models import Customer, Vehicle, Service

def show_menu():
    print("\n1. Customers")
    print("2. Vehicles")
    print("3. Services")
    print("0. Exit")

def get_choice():
    while True:
        try:
            choice = int(input("Choice: "))
            return choice
        except ValueError:
            print("Invalid input, try again")

def show_customers():
    customers = Customer.get_all()
    if customers:
        for c in customers:
            print(f"{c.id}: {c.name} - {c.phone}")
    else:
        print("No customers found")

def find_customer():
    try:
        id = int(input("Customer ID: "))
        customer = Customer.find_by_id(id)
        if customer:
            print(f"Found: {customer.name}")
        else:
            print("Not found")
    except ValueError:
        print("Invalid ID")

def add_customer():
    try:
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        Customer.create(name=name, phone=phone, email=email)
        print("Added!")
    except ValueError as e:
        print(f"Error: {e}")

def remove_customer():
    try:
        id = int(input("Customer ID: "))
        customer = Customer.find_by_id(id)
        if customer:
            customer.delete()
            print("Deleted!")
        else:
            print("Not found")
    except ValueError:
        print("Invalid ID")

def view_customer_vehicles():
    try:
        id = int(input("Customer ID: "))
        from db.models import Session
        session = Session()
        customer = session.query(Customer).filter_by(id=id).first()
        if customer:
            if customer.vehicles:
                for v in customer.vehicles:
                    print(f"{v.id}: {v.make} {v.model}")
            else:
                print("No vehicles found for this customer")
        else:
            print("Customer not found")
        session.close()
    except ValueError:
        print("Invalid ID")

def show_vehicles():
    vehicles = Vehicle.get_all()
    if vehicles:
        for v in vehicles:
            print(f"{v.id}: {v.make} {v.model} {v.year}")
    else:
        print("No vehicles found")

def find_vehicle():
    try:
        id = int(input("Vehicle ID: "))
        vehicle = Vehicle.find_by_id(id)
        if vehicle:
            print(f"Found: {vehicle.make} {vehicle.model}")
        else:
            print("Not found")
    except ValueError:
        print("Invalid ID")

def add_vehicle():
    try:
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        customer_id = int(input("Customer ID: "))
        Vehicle.create(make=make, model=model, year=year, customer_id=customer_id)
        print("Added!")
    except ValueError as e:
        print(f"Error: {e}")

def remove_vehicle():
    try:
        id = int(input("Vehicle ID: "))
        vehicle = Vehicle.find_by_id(id)
        if vehicle:
            vehicle.delete()
            print("Deleted!")
        else:
            print("Not found")
    except ValueError:
        print("Invalid ID")

def view_vehicle_services():
    try:
        id = int(input("Vehicle ID: "))
        from db.models import Session
        session = Session()
        vehicle = session.query(Vehicle).filter_by(id=id).first()
        if vehicle:
            if vehicle.services:
                for s in vehicle.services:
                    print(f"{s.id}: {s.description}")
            else:
                print("No services found for this vehicle")
        else:
            print("Vehicle not found")
        session.close()
    except ValueError:
        print("Invalid ID")

def show_services():
    services = Service.get_all()
    if services:
        for s in services:
            cost_display = f"${s.cost/100:.2f}" if s.cost else "$0.00"
            print(f"{s.id}: {s.description} - {cost_display}")
    else:
        print("No services found")

def find_service():
    try:
        id = int(input("Service ID: "))
        service = Service.find_by_id(id)
        if service:
            print(f"Found: {service.description}")
        else:
            print("Not found")
    except ValueError:
        print("Invalid ID")

def add_service():
    try:
        desc = input("Description: ")
        cost = int(float(input("Cost: ")) * 100)
        vehicle_id = int(input("Vehicle ID: "))
        Service.create(description=desc, cost=cost, vehicle_id=vehicle_id)
        print("Added!")
    except ValueError as e:
        print(f"Error: {e}")

def remove_service():
    try:
        id = int(input("Service ID: "))
        service = Service.find_by_id(id)
        if service:
            service.delete()
            print("Deleted!")
        else:
            print("Not found")
    except ValueError:
        print("Invalid ID")

def view_service_vehicle():
    try:
        id = int(input("Service ID: "))
        from db.models import Session
        session = Session()
        service = session.query(Service).filter_by(id=id).first()
        if service and service.vehicle:
            v = service.vehicle
            print(f"Vehicle: {v.make} {v.model}")
        else:
            print("Not found")
        session.close()
    except ValueError:
        print("Invalid ID")

def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. View All")
        print("2. Find by ID")
        print("3. Add New")
        print("4. Delete")
        print("5. View Vehicles")
        print("0. Back")
        c = get_choice()
        if c == 1: show_customers()
        elif c == 2: find_customer()
        elif c == 3: add_customer()
        elif c == 4: remove_customer()
        elif c == 5: view_customer_vehicles()
        elif c == 0: break
        else: print("Invalid choice")

def vehicle_menu():
    while True:
        print("\nVehicle Menu:")
        print("1. View All")
        print("2. Find by ID")
        print("3. Add New")
        print("4. Delete")
        print("5. View Services")
        print("0. Back")
        c = get_choice()
        if c == 1: show_vehicles()
        elif c == 2: find_vehicle()
        elif c == 3: add_vehicle()
        elif c == 4: remove_vehicle()
        elif c == 5: view_vehicle_services()
        elif c == 0: break
        else: print("Invalid choice")

def service_menu():
    while True:
        print("\nService Menu:")
        print("1. View All")
        print("2. Find by ID")
        print("3. Add New")
        print("4. Delete")
        print("5. View Vehicle")
        print("0. Back")
        c = get_choice()
        if c == 1: show_services()
        elif c == 2: find_service()
        elif c == 3: add_service()
        elif c == 4: remove_service()
        elif c == 5: view_service_vehicle()
        elif c == 0: break
        else: print("Invalid choice")

def run():
    while True:
        show_menu()
        choice = get_choice()
        
        if choice == 1:
            customer_menu()
        elif choice == 2:
            vehicle_menu()
        elif choice == 3:
            service_menu()
        elif choice == 0:
            break