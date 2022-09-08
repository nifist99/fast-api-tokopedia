from schema.ConnectionDB import Base,engine

Base.metadata.drop_all(engine)