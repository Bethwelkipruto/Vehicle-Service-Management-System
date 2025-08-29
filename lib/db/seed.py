from models import Base, Customer, Vehicle, Service, engine, Session

def seed():
    Base.metadata.create_all(engine)
    session = Session()
    
    session.query(Service).delete()
    session.query(Vehicle).delete()
    session.query(Customer).delete()
    
    c1 = Customer(name="John", phone="123", email="john@test.com")
    c2 = Customer(name="Jane", phone="456", email="jane@test.com")
    session.add_all([c1, c2])
    session.commit()
    
    v1 = Vehicle(make="Toyota", model="Camry", year=2020, customer_id=1)
    v2 = Vehicle(make="Honda", model="Civic", year=2019, customer_id=2)
    session.add_all([v1, v2])
    session.commit()
    
    s1 = Service(description="Oil Change", cost=3500, vehicle_id=1)
    s2 = Service(description="Brake Check", cost=8000, vehicle_id=2)
    session.add_all([s1, s2])
    session.commit()
    
    print("Done!")
    session.close()

if __name__ == "__main__":
    seed()