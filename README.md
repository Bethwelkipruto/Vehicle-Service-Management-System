# Vehicle Service Management System

A Python CLI application for managing vehicle service records, built with SQLAlchemy ORM and Alembic migrations.

## Description

This application allows users to manage customers, their vehicles, and service records through an interactive command-line interface. It demonstrates object-oriented programming principles, database relationships, and input validation.

## Features

### Customer Management
- Create new customers with name, phone, and email
- View all customers
- Find customers by ID
- Delete customers (cascades to their vehicles and services)
- View all vehicles owned by a customer

### Vehicle Management
- Create new vehicles with make, model, year, license plate, and owner
- View all vehicles with owner information
- Find vehicles by ID
- Delete vehicles (cascades to their services)
- View all services performed on a vehicle

### Service Management
- Create new service records with description, cost, and vehicle
- View all services with vehicle information
- Find services by ID
- Delete service records
- View the vehicle associated with a service

## Data Model

The application uses three main models with the following relationships:

- **Customer** (1) → (many) **Vehicle**: One customer can own multiple vehicles
- **Vehicle** (1) → (many) **Service**: One vehicle can have multiple service records

### Model Constraints
- Customer names must be at least 2 characters
- Email addresses must be in valid format
- Vehicle years must be between 1900 and 2030
- Service costs cannot be negative

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pipenv install
   ```
3. Set up the database:
   ```bash
   cd lib/db
   pipenv run alembic upgrade head
   pipenv run python seed.py
   ```

## Usage

Run the CLI application:
```bash
cd lib
pipenv run python cli.py
```

Navigate through the menus to:
1. Choose Customer, Vehicle, or Service management
2. Select operations: view all, find by ID, create, delete, or view related objects
3. Follow prompts with input validation

## File Structure

```
lib/
├── cli.py              # Main CLI entry point
├── helpers.py          # CLI functions and menus
└── db/
    ├── models.py       # SQLAlchemy models with ORM methods
    ├── seed.py         # Database seeding script
    ├── alembic.ini     # Alembic configuration
    └── migrations/     # Database migration files
```

## Dependencies

- SQLAlchemy: ORM for database operations
- Alembic: Database migration management
- Python 3.8+

## Error Handling

The application includes comprehensive input validation:
- Invalid menu choices prompt for re-entry
- Required fields are validated
- Database constraints are enforced
- Foreign key relationships are verified before creation
- Confirmation prompts for deletions