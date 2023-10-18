import sqlalchemy as db
engine = db.create_engine(
    'postgresql+psycopg2://postgres:123xensa@localhost:3211/memorise')
