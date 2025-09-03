from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)
    
    vehicles = relationship("Vehicle", back_populates="customer")
    
    def __init__(self, name, phone=None, email=None):
        if not name or len(name) < 2:
            raise ValueError("Name too short")
        self.name = name
        self.phone = phone
        self.email = email
    
    @classmethod
    def create(cls, name, phone=None, email=None):
        session = Session()
        customer = cls(name=name, phone=phone, email=email)
        session.add(customer)
        session.commit()
        session.refresh(customer)  
        customer_id = customer.id
        session.close()
        return cls.find_by_id(customer_id)  
    
    @classmethod
    def get_all(cls):
        session = Session()
        customers = session.query(cls).all()
        session.close()
        return customers
    
    @classmethod
    def find_by_id(cls, id):
        session = Session()
        customer = session.query(cls).filter_by(id=id).first()
        session.close()
        return customer
    
    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()

class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    license_plate = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    customer = relationship("Customer", back_populates="vehicles")
    services = relationship("Service", back_populates="vehicle")
    
    def __init__(self, make, model, year=None, license_plate=None, customer_id=None):
        if year and (year < 1900 or year > 2030):
            raise ValueError("Invalid year")
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.customer_id = customer_id
    
    @classmethod
    def create(cls, make, model, year=None, license_plate=None, customer_id=None):
        session = Session()
        vehicle = cls(make=make, model=model, year=year, license_plate=license_plate, customer_id=customer_id)
        session.add(vehicle)
        session.commit()
        session.refresh(vehicle)
        vehicle_id = vehicle.id
        session.close()
        return cls.find_by_id(vehicle_id)
    
    @classmethod
    def get_all(cls):
        session = Session()
        vehicles = session.query(cls).all()
        session.close()
        return vehicles
    
    @classmethod
    def find_by_id(cls, id):
        session = Session()
        vehicle = session.query(cls).filter_by(id=id).first()
        session.close()
        return vehicle
    
    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()

class Service(Base):
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    cost = Column(Integer)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    
    vehicle = relationship("Vehicle", back_populates="services")
    
    def __init__(self, description, cost=None, vehicle_id=None):
        if cost and cost < 0:
            raise ValueError("Cost cannot be negative")
        self.description = description
        self.cost = cost
        self.vehicle_id = vehicle_id
    
    @classmethod
    def create(cls, description, cost=None, vehicle_id=None):
        session = Session()
        service = cls(description=description, cost=cost, vehicle_id=vehicle_id)
        session.add(service)
        session.commit()
        session.refresh(service)
        service_id = service.id
        session.close()
        return cls.find_by_id(service_id)
    
    @classmethod
    def get_all(cls):
        session = Session()
        services = session.query(cls).all()
        session.close()
        return services
    
    @classmethod
    def find_by_id(cls, id):
        session = Session()
        service = session.query(cls).filter_by(id=id).first()
        session.close()
        return service
    
    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()

import os
db_path = os.path.join(os.path.dirname(__file__), 'vehicle_service.db')
engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)