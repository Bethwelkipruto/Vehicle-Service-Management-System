import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'db'))

from db.models import Customer, Vehicle, Service


main_options = {1: "Customers", 2: "Vehicles", 3: "Services", 0: "Exit"}
sub_options = ["View All", "Find by ID", "Add New", "Delete", "View Related", "Back"]
valid_choices = (1, 2, 3, 4, 5, 0)

def show_menu():
    print("\nMain Menu:")
    for key, value in main_options.items():
        print(f"{key}. {value}")

def get_choice():
    while True:
        try:
            choice = int(input("Choice: "))
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice, try again")
        except ValueError:
            print("Please enter a number")

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
        print("\nEnter customer details:")
        name = input("Name (minimum 2 characters): ").strip()
        if not name:
            print("Name is required")
            return
        phone = input("Phone (optional): ").strip() or None
        email = input("Email (optional): ").strip() or None
        Customer.create(name=name, phone=phone, email=email)
        print(f"✓ Customer '{name}' added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def remove_customer():
    try:
        id = int(input("Customer ID to delete: "))
        customer = Customer.find_by_id(id)
        if customer:
            confirm = input(f"Delete customer '{customer.name}'? (y/N): ").lower()
            if confirm == 'y':
                customer.delete()
                print("✓ Customer deleted successfully!")
            else:
                print("Deletion cancelled")
        else:
            print("Customer not found")
    except ValueError:
        print("Invalid ID format")

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
        print("\nEnter vehicle details:")
        make = input("Make: ").strip()
        model = input("Model: ").strip()
        if not make or not model:
            print("Make and model are required")
            return
        year = int(input("Year (1900-2030): "))
        license_plate = input("License plate (optional): ").strip() or None
        customer_id = int(input("Customer ID: "))
        Vehicle.create(make=make, model=model, year=year, license_plate=license_plate, customer_id=customer_id)
        print(f"✓ Vehicle '{make} {model}' added successfully!")
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
        print("\nEnter service details:")
        desc = input("Description: ").strip()
        if not desc:
            print("Description is required")
            return
        cost_input = input("Cost (optional, enter 0 for free): ").strip()
        cost = int(float(cost_input) * 100) if cost_input else 0
        vehicle_id = int(input("Vehicle ID: "))
        Service.create(description=desc, cost=cost, vehicle_id=vehicle_id)
        print(f"✓ Service '{desc}' added successfully!")
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
    menu_actions = {
        1: show_customers,
        2: find_customer, 
        3: add_customer,
        4: remove_customer,
        5: view_customer_vehicles
    }
    
    while True:
        print("\nCustomer Menu:")
        for i, option in enumerate(sub_options):
            print(f"{i+1 if i < 5 else 0}. {option}")
        
        choice = get_choice()
        if choice == 0:
            break
        elif choice in menu_actions:
            menu_actions[choice]()
        else:
            print("Invalid choice")

def vehicle_menu():
    menu_actions = {
        1: show_vehicles,
        2: find_vehicle,
        3: add_vehicle, 
        4: remove_vehicle,
        5: view_vehicle_services
    }
    
    while True:
        print("\nVehicle Menu:")
        for i, option in enumerate(sub_options):
            print(f"{i+1 if i < 5 else 0}. {option}")
        
        choice = get_choice()
        if choice == 0:
            break
        elif choice in menu_actions:
            menu_actions[choice]()
        else:
            print("Invalid choice")

def service_menu():
    menu_actions = {
        1: show_services,
        2: find_service,
        3: add_service,
        4: remove_service, 
        5: view_service_vehicle
    }
    
    while True:
        print("\nService Menu:")
        for i, option in enumerate(sub_options):
            print(f"{i+1 if i < 5 else 0}. {option}")
        
        choice = get_choice()
        if choice == 0:
            break
        elif choice in menu_actions:
            menu_actions[choice]()
        else:
            print("Invalid choice")

def run():
    main_actions = {
        1: customer_menu,
        2: vehicle_menu,
        3: service_menu
    }
    
    while True:
        show_menu()
        choice = get_choice()
        
        if choice == 0:
            print("Thank you for using Vehicle Service Management System!")
            break
        elif choice in main_actions:
            main_actions[choice]()
        else:
            print("Invalid choice, please try again")