from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

engine = create_engine(current_app.config["DATABASE_URI"], pool_pre_ping=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


def save_model(model):
    session.add(model)
    session.commit()


def save_models(models):
    session.bulk_save_objects(models)
    session.commit()


def commit():
    session.commit()


Base.save = save_model
Base.save_all = save_models
Base.commit = staticmethod(commit)


def init_schema():
    import application.models

    Base.metadata.create_all(bind=engine)
