from app.db.database import SessionLocal, Base, engine
from app.models.customer import Customer
from app.models.menu import MenuItem


def seed_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        if db.query(Customer).count() == 0:
            db.add_all([
                Customer(name="Aisha", phone="0123456789", address="Rawang"),
                Customer(name="Daniel", phone="0198887777", address="Bangsar South"),
            ])

        if db.query(MenuItem).count() == 0:
            db.add_all([
                MenuItem(name="Nasi Lemak", description="Rice with sambal, egg and anchovies", price=8.50),
                MenuItem(name="Chicken Burger", description="Grilled chicken burger", price=12.90),
                MenuItem(name="Teh Ais", description="Iced milk tea", price=3.50),
                MenuItem(name="Mee Goreng", description="Fried noodles", price=9.00),
            ])

        db.commit()
        print("Seed data inserted successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
