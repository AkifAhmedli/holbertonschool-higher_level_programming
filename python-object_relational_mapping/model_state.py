#!/usr/bin/python3
"""
State sinifinin tərifini və Base = declarative_base() nümunəsini
ehtiva edən Python faylı.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Bütün model siniflərimizin miras alacağı əsas sinif
Base = declarative_base()


class State(Base):
    """
    State sinifi:
    - MySQL-dəki 'states' cədvəlinə bağlanır.
    - id: unikal tam ədəd, primary key, null ola bilməz.
    - name: maksimum 128 simvollu sətir, null ola bilməz.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
