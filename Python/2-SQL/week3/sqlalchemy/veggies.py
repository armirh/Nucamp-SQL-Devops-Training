from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to Postgres database
engine = create_engine('postgresql://postgres@localhost:5432/week3')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Veggie(Base):
    __tablename__ = "veggies"

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    color = Column(String, nullable=False)
    name = Column(String, nullable=False)


# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'name': 'carrot', 'color': 'orange'},
    {'name': 'onion', 'color': 'yellow'},
    {'name': 'onion', 'color': 'red'},
    {'name': 'zucchini', 'color': 'green'},
    {'name': 'squash', 'color': 'yellow'},
    {'name': 'pepper', 'color': 'red'},
    {'name': 'pepper', 'color': 'green'},
    {'name': 'pepper', 'color': 'orange'},
    {'name': 'pepper', 'color': 'yellow'},
    {'name': 'onion', 'color': 'white'},
    {'name': 'green bean', 'color': 'green'},
    {'name': 'jicama', 'color': 'tan'},
    {'name': 'tomatillo', 'color': 'green'},
    {'name': 'radicchio', 'color': 'purple'},
    {'name': 'potato', 'color': 'brown'}
]

# Turn the seed data into a list of Veggie objects
veggie_objects = []
for item in seed_data:
    v = Veggie(name=item["name"], color=item["color"])
    veggie_objects.append(v)

# Create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(veggie_objects)
session.commit()


# Create a new session for performing queries
session = Session()

# SELECT * FROM veggies
veggies = session.query(Veggie).all()

print('INSERTED VEGGIES:', veggies)
print('')  # separator

for v in veggies:
    print(v.color, v.name)

print('')  # separator

# SELECT * FROM veggies ORDER BY name, color
veggies = session.query(Veggie).order_by(
    Veggie.name, Veggie.color).all()

for i, v in enumerate(veggies):
    print(str(i+1) + ". " + v.formatted_name())
