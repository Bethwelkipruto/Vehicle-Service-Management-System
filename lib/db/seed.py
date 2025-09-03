from models import Base, Customer, Vehicle, Service, engine, Session
from faker import Faker
import random

fake = Faker()

def seed():
    Base.metadata.create_all(engine)
    session = Session()
    
    session.query(Service).delete()
    session.query(Vehicle).delete() 
    session.query(Customer).delete()
    
    customers = []
    for i in range(5):
        customer = Customer(
            name=fake.name(),
            phone=fake.phone_number(),
            email=fake.email()
        )
        customers.append(customer)
    
    session.add_all(customers)
    session.commit()
    
    makes_models = [
        ("Toyota", ["Camry", "Corolla", "Prius", "RAV4"]),
        ("Honda", ["Civic", "Accord", "CR-V", "Pilot"]),
        ("Ford", ["F-150", "Escape", "Mustang", "Explorer"]),
        ("Chevrolet", ["Silverado", "Equinox", "Malibu", "Tahoe"])
    ]
    
    vehicles = []
    for customer in customers:
        for j in range(random.randint(1, 3)):
            make, models = random.choice(makes_models)
            vehicle = Vehicle(
                make=make,
                model=random.choice(models),
                year=random.randint(2015, 2024),
                license_plate=fake.license_plate(),
                customer_id=customer.id
            )
            vehicles.append(vehicle)
    
    session.add_all(vehicles)
    session.commit()
    
    service_list = [
        ("Oil Change", 3500, 5500),
        ("Brake Inspection", 8000, 12000),
        ("Tire Rotation", 2500, 4000),
        ("Battery Replacement", 15000, 25000),
        ("Air Filter Replacement", 2000, 3500),
        ("Transmission Service", 20000, 35000)
    ]
    
    services = []
    for vehicle in vehicles:
        for k in range(random.randint(1, 4)):
            service_type, min_cost, max_cost = random.choice(service_list)
            service = Service(
                description=service_type,
                cost=random.randint(min_cost, max_cost),
                vehicle_id=vehicle.id
            )
            services.append(service)
    
    session.add_all(services)
    session.commit()
    
    print(f"Created {len(customers)} customers, {len(vehicles)} vehicles, {len(services)} services")
    session.close()

if __name__ == "__main__":
    seed()