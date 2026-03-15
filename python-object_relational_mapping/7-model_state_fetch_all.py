#!/usr/bin/python3
"""
'hbtn_0e_6_usa' bazasından bütün State obyektlərini 
SQLAlchemy vasitəsilə çəkən və siyahılayan skript.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Verilənlər bazası mühərriki (engine) yaradılır
    # Format: mysql+mysqldb://user:password@localhost:3306/dbname
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Sessiya (Session) sinifi yaradılır və mühərrikə bağlanır
    Session = sessionmaker(bind=engine)
    # Faktiki sessiya nümunəsi yaradılır
    session = Session()

    # Bütün State obyektlərini id-yə görə artan sıra ilə sorğulayırıq
    # Bu, SQL-dəki "SELECT * FROM states ORDER BY id ASC" əmrinə bərabərdir
    states = session.query(State).order_by(State.id).all()

    # Nəticələri tələb olunan formatda çap edirik
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Sessiyanı bağlayırıq
    session.close()
