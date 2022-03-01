from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app
import pytest


@pytest.fixture()
def app() -> Flask:
    '''Application instance'''
    
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    '''test client'''
    return app.test_client()


@pytest.fixture()
def runner(app):
    '''test runner'''
    return app.test_cli_runner()


@pytest.fixture()
def database(app):
    '''Database fixture'''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/acmevita_fixture.db'
    return SQLAlchemy(app)


@pytest.fixture(scope="module")
def fill_database(database):
    '''fill database'''
    import models
    from data.add_data import execute
    execute(database, models)
