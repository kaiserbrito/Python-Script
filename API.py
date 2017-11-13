from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_database
from sqlalchemy.orm import sessionmaker
import jenkins
import requests
import datetime

Base = declarative_database()

def iniDB():
    """ Function to initialize the SqLite """
    engine = create_engine('sqlite:///cli.db', echo=False)
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    return session


def jenkins_connection(url, username, password):
    """ Function to connect the Jenkins API """
    server = jenkins.Jenkins(url)
    username = username
    password = password
    return server

def add_job(session, joblist):
    """ Function to Add a Job in the job list """
    for job in joblist:
        session.add(job)
    session.commit()

def get_job(session, name):
    """ Function to get a previous job """
    job = session.query(Jobs).filter_by(name=name).order_by(Jobs.jen_id_desc()).first()
    if (job != None):
        return jon.jen_id
    else:
        return None

